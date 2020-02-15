from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import *
from django.contrib import messages

def index(request):
    return redirect('/shows')

def display(request):
    context={
        "shows": Show.objects.all()
    }
    return render (request, 'display.html', context)


def create(request):
    errors = Show.objects.basic_validator(request.POST)
    
    if "title_exist" in errors:
    
        return JsonResponse(
            {
                "YOUR INPUT": "NOT UNIQUE"
            }
        )
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)  
        return redirect('/shows')

    if len(request.POST['description'])>0:
        new_show=Show.objects.create(
        title=request.POST['title'], 
        network=request.POST['network'], 
        release_date=request.POST['release_date'], 
        description=request.POST['description'] 
        )
    elif len(request.POST['description'])<=0:
        new_show=Show.objects.create(
        title=request.POST['title'], 
        network=request.POST['network'], 
        release_date=request.POST['release_date']
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
    errors = Show.objects.basic_validator(request.POST)
    
    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request,v)
        return redirect('/shows')

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

def titletest(request):
    results = Show.objects.filter(title=request.POST['title'])
    if len(results) > 0:
        return JsonResponse(
            {
                "error":"Title Exists"
            }
        )
    else:
        return JsonResponse(
            {
                "success":"OK"
            }
        )

def secret_page(request):
    return render(request, "secret_page.html")