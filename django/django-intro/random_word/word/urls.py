from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('generate', views.reset_answer),
    path('reset', views.reset_attempts)
]