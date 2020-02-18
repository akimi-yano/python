from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('validate', views.validate),
    path('success_login', views.success_login),
    path('success_register', views.success_register),
    path('logout', views.logout),
    path('show_uniqueness_error', views.show_uniqueness_error)
]
