from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/submit_message', views.submit_message),
    path('/submit_comment', views.submit_comment),
    path('/delete_message', views.delete_message)
    
]
