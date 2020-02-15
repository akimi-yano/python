from django.db import models
from datetime import datetime
from dateutil import parser
from django.http import JsonResponse


class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title'])<2:
            errors['title'] = "Title must be at least 2 characters"

        if len(Show.objects.filter(title=post_data['title'])) > 0:
            errors['title_exist'] = "The title already exists"
      

        if len(post_data['network'])<3:
            errors['network'] = "Network must be at least 3 characters"

        if len(post_data['description'])>0:
            if len(post_data['description'])<10:
                errors['description'] = "Description must be at least 10 characters"
        
        # Can do this to make sure that the date is in the past #1
        # if parser.parse(post_data['release_date'])>=datetime.now():
        #     errors['release_date'] = "Release Date must be in the past"

        # Can do this to make sure that the date is in the past #2
        if datetime.strptime(post_data['release_date'],"%Y-%m-%d")>=datetime.now():
            errors['release_date'] = "Release Date must be in the past"
        

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)      

  
    objects = ShowManager()

