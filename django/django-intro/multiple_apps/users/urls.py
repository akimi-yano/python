from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('users', views.users),
    path('users/new', views.register),
    path('', views.redirect_to_blog)
]

