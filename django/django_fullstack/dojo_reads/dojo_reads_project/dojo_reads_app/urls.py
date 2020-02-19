
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/add', views.add_submission),
    path('/<int:book_id>', views.details),
    path('/send_add', views.send_add),
    path('/add_review/<int:book_id>', views.add_review),
    path('/delete/<int:review_id>', views.delete)
]