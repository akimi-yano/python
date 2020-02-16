from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('/add_books',views.add_books),
    path('/<int:book_id>',views.more_info),
    path('/add_fav/<int:book_id>',views.add_fav),
    path('/unfav/<int:book_id>',views.unfav),
    path('/edit_book/<int:book_id>', views.edit_book),
    path('/delete_book/<int:book_id>',  views.delete_book),
    path('/fav_page',views.fav_page)
]