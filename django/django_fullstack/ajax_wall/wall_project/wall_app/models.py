from django.db import models
from login_registration_app.models import *

class Message(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message=models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)