from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from chat.models.models import Message, User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import json


@login_required
def chatroom(request, pk: int):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) | Q(sender=other_user, receiver=request.user)
    )
    messages.update(seen=True)

    # For chatpage
    current_user = request.user
    receiver_ids_sent = Message.objects.filter(sender=current_user).values_list('receiver', flat=True).distinct()
    sender_ids_received = Message.objects.filter(receiver=current_user).values_list('sender', flat=True).distinct()
    combined_user_ids = set(receiver_ids_sent) | set(sender_ids_received)
    users_info = User.objects.filter(id__in=combined_user_ids).values('id', 'username', 'first_name', 'last_name')

    return render(request, 'chat/chatroom.html',
                  {'other_user': other_user, 'messages': messages, 'users_info': users_info, 'user': current_user})


@login_required
def ajax_load_messages(request, pk):
    other_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False).filter(Q(sender=other_user, receiver=request.user))

    message_list = [{
        "sender": message.sender.username,
        "receiver": message.receiver.username,
        "sent": message.sender == request.user,
    } for message in messages]
    messages.update(seen=True)
    if request.method == 'POST':
        message = json.loads(request.body.decode('utf-8'))
        m = Message.objects.create(sender=request.user, receiver=other_user, message=message)
        message_list.append({
            "sender": request.user.username,
            "message": m.message,
            "sent": True,
        })
    return JsonResponse(message_list, safe=False)


def chatpage(request):
    current_user = request.user

    # Retrieve distinct receiver IDs where the current user is the sender
    receiver_ids_sent = Message.objects.filter(sender=current_user).values_list('receiver', flat=True).distinct()

    # Retrieve distinct sender IDs where the current user is the receiver
    sender_ids_received = Message.objects.filter(receiver=current_user).values_list('sender', flat=True).distinct()

    # Combine the sender and receiver IDs
    combined_user_ids = set(receiver_ids_sent) | set(sender_ids_received)

    # Retrieve user IDs and usernames associated with combined IDs
    users_info = User.objects.filter(id__in=combined_user_ids).values('id', 'username', 'first_name', 'last_name')

    return render(request, 'chat/chatpage.html', {'users_info': users_info, 'user': current_user})
