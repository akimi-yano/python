from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('songs',views.songs),
    path('new',views.new),
    path('songs/<int:song_id>', views.show),
    path('edit/<int:song_id>',views.edit),
    path('delete/<int:song_id>',views.delete),
    path('create_process', views.create_process),
    path('update_process', views.update_process)
    
]