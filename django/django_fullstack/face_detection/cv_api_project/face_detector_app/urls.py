from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('face_detection/detect', views.detect)
]
