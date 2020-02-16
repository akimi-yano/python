from django.db import models
from login_registration_app.models import *

class BookManager(models.Manager):
    def book_validator(self, post_data):
        errors = {}
        
        if len(post_data['title'])<1:
            errors['title'] = "Title is required"
        
        if len(post_data['description'])<5:
            errors['description'] = "Description must be at least 5 characters"
            
        return errors
        

class Book(models.Model):
    title = models.CharField(max_length= 60)
    description = models.TextField()
    users_who_liked = models.ManyToManyField(User, related_name="books_liked")
    user_who_uploaded = models.ForeignKey(User, related_name="bookes_uploaded", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = BookManager()
    
    
    
