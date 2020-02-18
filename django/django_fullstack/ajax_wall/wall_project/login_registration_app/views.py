from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        birthday = request.POST['birthday'],
        password = pw_hash
        )
    
    return redirect('/success_register')

def success_register(request):
    return render(request, "success_register.html")

def validate(request):
    trying_user = User.objects.filter(email=request.POST['email'])
    if trying_user:
        logged_user=trying_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id']=logged_user.id
            return redirect('/success_login')
    return redirect('/')


def success_login(request):
    first_name = User.objects.get(id=request.session['user_id']).first_name
    context = {
        "first_name" : first_name
    }
    return redirect('/wall')


def logout(request):
    del request.session['user_id']
    return redirect('/')