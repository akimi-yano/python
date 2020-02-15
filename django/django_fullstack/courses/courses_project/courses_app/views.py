from django.shortcuts import render, HttpResponse, redirect
from .models import*
from django.contrib import messages

def index(request):
    context={
        "courses": Course.objects.all()
    }

    return render(request, "index.html", context)


def submit_course(request):
    errors = Course.objects.validator(request.POST)

    if len(errors)>0:
        for k, v in errors.items():
            messages.error(request, v)

        return redirect('/')

    if len(request.POST['description'])>0:
        new_course=Course.objects.create(
        name=request.POST['name'],
        description=request.POST['description']
        )

    elif len(request.POST['description'])<=0:
        new_course=Course.objects.create(
        name=request.POST['name']
        )
    return redirect('/')

