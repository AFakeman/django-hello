from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ToDoItem 

def index(request):
    return render(request, 'index.html')

def login_page(request):
    error = request.GET.get('error')
    context = {'error': error}
    return render(request, 'login.html', context)

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

def log_out(request):
    logout(request)
    return redirect('index')

def register_page(request):
    error = request.GET.get('error')
    context = {'error': error}
    return render(request, 'register.html', context)

def register(request):
    username = request.POST['login']
    password = request.POST['password']
    email = request.POST['email']
    try:
      user = User.objects.create_user(username, email, password)
    except IntegrityError:
      response = redirect('register_page')
      response['Location'] += '?error=true'
      return response
    user.save()
    auth_login(request, user)
    return redirect('index')

@login_required
def todo_view(request):
    query = ToDoItem.objects.filter(user=request.user).order_by('create_date')
    context = {'todo_items': query}
    return render(request, 'list.html', context)

@login_required
def add_todo(request):
    title = request.POST['title']
    ToDoItem(text=title, user=request.user).save()
    return redirect('todo_view')

@login_required
def apply_todo_changes(request):
    query = ToDoItem.objects.filter(user=request.user)
    for todo_item in query:
        if str(todo_item.id) in request.POST:
          todo_item.done = True
        else:
          todo_item.done = False
        todo_item.save()
        if str(todo_item.id) + '_delete' in request.POST:
          todo_item.delete()
    return redirect('todo_view')
