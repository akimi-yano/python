from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/<int:id>', views.show_books),
    path('books/<int:id>/add_author', views.add_author),
    path('submit_books', views.submit_books),
    path('authors', views.auths),
    path('submit_auths', views.submit_auths),
    path('authors/<int:id>/add_book', views.add_book),
    path('authors/<int:id>', views.show_auths),
]
