
from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.index),	
    path('submit_course', views.submit_course),
    path('remove_confirm/<int:id>', views.remove_confirm),
    path('remove/<int:id>', views.remove),
    path('show_form/<int:id>', views.show_form),
    path('courses/<int:id>/comments', views.comment),
    path('deleteajax', views.ajax_remove)

]