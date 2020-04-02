from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/add', views.add_form),
    path('/add_submit', views.add_process),
    path('/show/<int:event_id>', views.show_event),
    path('/edit/<int:event_id>', views.edit_event),
    path('/edit_submit/<int:event_id>', views.edit_process),
    path('/delete/<int:event_id>', views.delete_event),
    path('/join/<int:event_id>', views.join),
    path('/unjoin/<int:event_id>', views.unjoin),
    path('/join_list', views.list_join)
    
]
