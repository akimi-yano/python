from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/submit_message', views.submit_message),
    path('/submit_comment', views.submit_comment),
    path('/delete_message', views.delete_message),
    path('/addComment_ajax', views.addComment_ajax),
    path('/deleteComment_ajax', views.deleteComment_ajax),
    path('/deleteMessage_ajax', views.deleteMessage_ajax)
    
]
