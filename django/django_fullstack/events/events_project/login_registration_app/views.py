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
        password = pw_hash,
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
            return redirect('/events')
    messages.error(request, "invalid login")
    return redirect('/')


def success_login(request):
    first_name = User.objects.get(id=request.session['user_id']).first_name
    context = {
        "first_name" : first_name
    }
    return render(request, "success_login.html", context)


def logout(request):
    del request.session['user_id']
    return redirect('/')

def profile(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        my_interests=user.interests.all()
        my_interests_ids = [interest.id for interest in my_interests]
        other_interests=Interest.objects.all().exclude(id__in=my_interests_ids)
        context={
            "user": user,        
            "my_interests": my_interests,
            "other_interests": other_interests
        }
        return render(request, "profile.html", context)

def add_interests(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        if 'interests' in request.POST and len(request.POST['interests']) > 0:
            interest_ids = [int(interest_id) for interest_id in request.POST.getlist('interests')]
            interests = Interest.objects.filter(id__in=interest_ids).all()
            for interest in interests:
                user.interests.add(interest)
        if len(request.POST['new_interest']) > 0:
            if len(Interest.objects.filter(interest_name = request.POST['new_interest'])) == 0:
                new_interest = Interest.objects.create(interest_name = request.POST['new_interest'])
                user.interests.add(new_interest)
            else:
                messages.error(request, "The interest already exists")
        return redirect('/profile')

def remove_interest(request, interest_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        removed_interest = Interest.objects.get(id=interest_id)
        user.interests.remove(removed_interest)
        return redirect('/profile')
        

