from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages



def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user =User.objects.get(id=request.session['user_id'])
        context = {
            "events": Event.objects.all(),
        }
        return render(request, "event_list.html", context)

def add_form(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        return render(request, "add.html")

def add_process(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
 
        
        errors = Event.objects.event_validator(request.POST)
        if len(errors)>0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/events/add')
        
        user = User.objects.get(id=request.session['user_id'])
        new_event = Event.objects.create(
            event_name = request.POST['event_name'], 
            location = request.POST['location'], 
            start_date = request.POST['start_date'], 
            end_date = request.POST['end_date'], 
            organizer = user)
        new_event.participants.add(user)
        
        return redirect("/events")

def show_event(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:  
        context={
            'event': Event.objects.get(id=event_id),
            'user':  User.objects.get(id=request.session['user_id'])
        }
        return render(request, "show.html", context)

def edit_event(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context={
            'event': Event.objects.get(id=event_id)
        }
        return render(request, "edit.html", context)


def edit_process(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        
        errors = Event.objects.event_validator(request.POST)
        if len(errors)>0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(f'/events/edit/{event_id}')
        
        
        edited_event = Event.objects.get(id=event_id)
        print(edited_event)
        edited_event.event_name = request.POST['event_name']
        edited_event.location = request.POST['location']
        edited_event.start_date = request.POST['start_date']
        edited_event.end_date = request.POST['end_date']
        edited_event.save()
        return redirect(f'/events/show/{event_id}')


def delete_event(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        deleted_event = Event.objects.get(id=event_id)
        deleted_event.delete()
        return redirect("/events")


def join(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        event_to_join = Event.objects.get(id=event_id)
        event_to_join.participants.add(user)
        return redirect(f'/events/show/{event_id}')

def unjoin(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        event_to_join = Event.objects.get(id=event_id)
        event_to_join.participants.remove(user)
        return redirect(f'/events/show/{event_id}')
        
def list_join(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context={
            'events_to_join': user.joined_events.all()
        }
        return render(request, "join_list.html", context)