from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("This is the equivalent of @app.route('/')")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    # open question: why does '/' work and not ''?
    return redirect('/')

def show(reuqest, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redirect('/')
    #type '/delete', '/destroy'