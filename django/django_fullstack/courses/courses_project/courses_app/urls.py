
from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.index),	
    path('submit_course', views.submit_course),
    path('remove_confirm/<int:id>', views.remove_confirm),
    path('remove/<int:id>', views.remove)
]