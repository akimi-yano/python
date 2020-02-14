from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.display),
    path('shows/new', views.submit_new),
    path('shows/<int:id>', views.describe),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/delete', views.delete),
    path('show/data', views.create),
    path('show/update/<int:id>', views.submit_update)
]