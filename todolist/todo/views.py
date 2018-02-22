from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Test")

def login_page(request, error=None):
	return render(request, 'login.html')

def login(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('index')
    else:
        response = redirect('login_page')
        response['Location'] += '?error=bad_login'
        return response

def register_page(request):
    return render(request, 'register.html')

def register(request):
    username = request.POST['login']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect('register_page')
