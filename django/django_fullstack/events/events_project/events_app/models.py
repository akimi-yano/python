from django.db import models
from login_registration_app.models import *
from datetime import datetime



class EventManager(models.Manager):
    def event_validator(self, post_data):
        errors = {}
        if len(post_data['event_name'])<1:
            errors['event_name']="Event Name is required"
        if len(post_data['location'])<1:
            errors['location']="Location is required"
        if len(post_data['start_date'])<1:
            errors['start_date']="Start Date is required"
        if len(post_data['end_date'])<1:
            errors['end_date']="End Date is required"
        if len(post_data['start_date']) > 0 and len(post_data['end_date']) > 0:
            if post_data['end_date'] < post_data['start_date']:
                errors['end_before_start']="Start Date must be before End Date"    
            if datetime.strptime(post_data['end_date'],"%Y-%m-%d") <= datetime.now():
                errors['end_in_past']="End Date must be in the future" 
            if datetime.strptime(post_data['start_date'],"%Y-%m-%d") <= datetime.now():
                errors['start_in_past']="Start Date must be in the future" 
        return errors


class Event(models.Model):
    event_name = models.CharField(max_length= 60)
    location = models.CharField(max_length= 60)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    organizer = models.ForeignKey(User, related_name="organized_events", on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name="joined_events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventManager()
