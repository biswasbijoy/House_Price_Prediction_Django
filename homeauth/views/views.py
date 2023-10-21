from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def signUp(request):
    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirmPassword = request.POST['password2']
        user = User.objects.create_user(userName, email, password)
        user.first_name = firstName
        user.last_name = lastName
        if password != confirmPassword:
            return HttpResponse('Password does not match')
        user.save()
        return redirect('homeauth:login')

    return render(request, 'homeauth/signup.html')


def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('posts:home')
        else:
            return HttpResponse('Invalid Credentials')
    return render(request, 'homeauth/login.html')


def logOut(request):
    logout(request)
    return redirect('homeauth:login')


