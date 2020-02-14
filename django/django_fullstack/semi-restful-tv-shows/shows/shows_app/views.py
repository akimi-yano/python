from django.shortcuts import render, HttpResponse, redirect

from .models import *

def index(request):
    return redirect('/shows')

def display(request):
    
    context={
        "shows": Show.objects.all()
    }
    return render (request, 'display.html', context)


def create(request):
    new_show=Show.objects.create(
    title=request.POST['title'], 
    network=request.POST['network'], 
    release_date=request.POST['release_date'], 
    description=request.POST['description'] 
    )
    return redirect(f'/shows/{new_show.id}')


def submit_new(request):
    return render (request, 'create.html')



def describe(request, id):
    context={
    "show": Show.objects.get(id = id)
    }
    return render (request, 'describe.html', context)


def edit(request, id):
    context={
    "show": Show.objects.get(id = id)
    }
    return render (request, 'edit.html', context)

def submit_update(request, id):
    update = Show.objects.get(id=id)
    update.title=request.POST['title']
    update.network=request.POST['network']
    update.release_date=request.POST['release_date']
    update.description=request.POST['description'] 
    update.save()
   
    return redirect(f'/shows/{update.id}')

def delete(request, id):
    delete = Show.objects.get(id=id)
    delete.delete()

    return redirect('/shows')
