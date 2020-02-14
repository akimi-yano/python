from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context={
        "books": Book.objects.all()
    }
    
    return render(request, "index.html", context)

def show_books(request, id):
    context={
        "book": Book.objects.get(id=id),
        "auths": Author.objects.all()
    }

    return render(request, "book_details.html", context)

def submit_books(request):

    Book.objects.create(title = request.POST['title'], desc = request.POST['description'])

    return redirect('/')

def add_author(request, id):
    Book.objects.get(id=id).publishers.add(request.POST['author'])
    
    return redirect(f'/books/{id}')

def auths(request):
    context={
        "auths": Author.objects.all()
        
    }
    return render(request, "auths.html", context)

def submit_auths(request):
    Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])

    return redirect('/authors')


def add_book(request, id):
    Author.objects.get(id=id).books.add(request.POST['book'])
    return redirect(f'/authors/{id}')

def show_auths(request, id):
    context={
        "author": Author.objects.get(id=id),
        "books": Book.objects.all()
    }

    return render(request, "auth_details.html", context)
    
    