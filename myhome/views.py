from django.shortcuts import render


def start(request):
    return render(request, 'starting.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
