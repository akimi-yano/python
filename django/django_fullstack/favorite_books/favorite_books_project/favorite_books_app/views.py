from django.shortcuts import render, HttpResponse, redirect 
from django.contrib import messages
from .models import *

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context={
            "user": user,
            "books": Book.objects.all()
        }
        return render(request, "submit_book.html", context)

def add_books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        errors=Book.objects.book_validator(request.POST)
        
        if len(errors)>0:
            for k, v in errors.items():
                messages.error(request,v)
            return redirect('/books')
        
        new_book = Book.objects.create(
            title = request.POST['title'], 
            description = request.POST['description'],
            user_who_uploaded = User.objects.get(id=request.session['user_id']),
            )
        user = User.objects.get(id=request.session['user_id'])
        new_book.users_who_liked.add(user)

        return redirect('/books')


def more_info(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context={
            "book": Book.objects.get(id=book_id),
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, "more_info.html", context)

def add_fav(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        new_fav = Book.objects.get(id=book_id)
        new_fav.users_who_liked.add(user)
        
        return redirect('/books')


def unfav(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        unfav = Book.objects.get(id=book_id)
        unfav.users_who_liked.remove(user)
        
        return redirect('/books')

def edit_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        errors=Book.objects.book_validator(request.POST)
        
        if len(errors)>0:
            for k, v in errors.items():
                messages.error(request,v)
            return redirect(f'/books/{book_id}')
        
        edited_book = Book.objects.get(id=book_id)
        edited_book.title = request.POST['title']
        edited_book.description = request.POST['description']
        edited_book.save()
        
        return redirect('/books')

def delete_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        deleted_book = Book.objects.get(id=book_id)
        deleted_book.delete()
        
        return redirect('/books')

def fav_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context={
            "fav_books": user.books_liked.all()
        }
        return render(request, "fav_page.html", context)
