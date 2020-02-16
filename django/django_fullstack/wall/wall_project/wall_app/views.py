from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime, timedelta, timezone

def index(request):
    user = User.objects.get(id=request.session['user_id'])
    messages = Message.objects.all()
    context={
        "user":user,
        "messages":messages,
        "thirty_min_ago": (datetime.now() - timedelta(minutes=30)).replace(tzinfo=timezone.utc)
    }
    return render(request,"wall.html", context)

def submit_message(request):
    user = User.objects.get(id=request.session['user_id'])
    new_message = Message.objects.create(text=request.POST['message'], user=user)
    return redirect('/wall')

def submit_comment(request):
    message_id = request.POST['message_id']
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    new_comment = Comment.objects.create(text=request.POST['comment'], user=user, message=message)
    return redirect('/wall')

def delete_message(request):
    message_id = request.POST['message_id']
    user = User.objects.get(id=request.session['user_id'])
    message_to_delete = Message.objects.get(id=message_id)

    thirty_min = datetime.now()  - timedelta(minutes=30)
    if message_to_delete.user == user and message_to_delete.created_at.replace(tzinfo=None) > thirty_min:
        message_to_delete.delete()
    return redirect('/wall')
    

