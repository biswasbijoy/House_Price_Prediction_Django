from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def landing_page(request):
    return render(request, 'landing_page.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
