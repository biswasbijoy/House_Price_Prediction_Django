from django.shortcuts import render


def start(request):
    return render(request, 'starting.html')


def auth(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'auth.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
