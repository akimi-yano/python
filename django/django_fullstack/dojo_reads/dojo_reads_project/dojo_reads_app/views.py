from django.shortcuts import render, HttpResponse, redirect
from .models import *



def index(request):
     print("in index")
     user = User.objects.get(id=request.session['user_id'])
     
     recent_reviews = Review.objects.all().order_by('-created_at').all()[:3]

     recently_reviewed_book_ids = [review.book.id for review in recent_reviews]
     other_books = Book.objects.exclude(id__in=recently_reviewed_book_ids)
     
     context={
          "books": other_books,
          "reviews": recent_reviews,
          "user": user
     }
     
     
     return render(request, "book_list.html", context)

def add_submission(request):
     context = {
          "range": range(1,6),
          "authors": Author.objects.all()
     }
     return render(request, "add.html", context)

def details(request, book_id):
     context ={
          "book": Book.objects.get(id = book_id),
          "range": range(1,6)
     }
     return render(request, "details.html", context)

def send_add(request):
     if len(request.POST['choose_author'])>0:
          author = Author.objects.get(id = request.POST['choose_author'])
          
     elif len(request.POST['choose_author']) <=0 and len(request.POST['type_author'])>0:
          author = Author.objects.create(name = request.POST['type_author'])     
     
     new_book = Book.objects.create(
          title = request.POST['title'], 
          author = author)
     
     new_review = Review.objects.create(
          text = request.POST['review'], 
          rating = request.POST['rating'], 
          user = User.objects.get(id=request.session['user_id']), 
          book = new_book)
     
     return redirect('/books')

def add_review(request, book_id):
     new_review = Review.objects.create(
          text = request.POST['review'], 
          rating = request.POST['rating'], 
          user = User.objects.get(id=request.session['user_id']), 
          book = Book.objects.get(id=book_id))


     return redirect('/books')

def delete(request, review_id):
     deleted_review = Review.objects.get(id=review_id)
     deleted_review.delete()
     return redirect('/books')


