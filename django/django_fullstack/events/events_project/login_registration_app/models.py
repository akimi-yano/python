from django.db import models
import re
from datetime import datetime, date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['first_name'])<2:
            errors['first_name']="First Name must be at least 2 characters"
            
        if not post_data['first_name'].isalpha():
            errors['first_name_not_str']="First Name must only contain letters"
            
        if len(post_data['last_name'])<2:
            errors['last_name']="Last Name must be at least 2 characters"
        
        if not post_data['last_name'].isalpha():
            errors['last_name_not_str']="Last Name must only contain letters"
            
        if len(post_data['password'])<8:
            errors['password']="Password must be at least 8 characters"    
                
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']="Email must be in a valid format"
            
        if len(User.objects.filter(email=post_data['email'])):
            errors['email_exist']="Email already exists"
            
        if post_data['confirm_pw'] != post_data['password']:
            errors['pw_unmatch']="Confirmation Password does not match with Password"
                    
            
        return errors


class User(models.Model):
    first_name = models.CharField(max_length= 60)
    last_name = models.CharField(max_length= 60)
    email = models.CharField(max_length= 60)
    password = models.CharField(max_length= 60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
class Interest(models.Model):
    interest_name = models.CharField(max_length= 60)
    interested_users = models.ManyToManyField(User, related_name="interests")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

