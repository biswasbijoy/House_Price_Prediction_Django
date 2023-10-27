from django.urls import path
from chat.views.views import *

app_name = 'chats'

urlpatterns = [
    path('chat/<int:pk>/', chatroom, name='chatroom'),
    path('chat/ajax/<int:pk>/', ajax_load_messages, name='chatroom-ajax'),
    path('chatpage', chatpage, name='chatpage'),
]
