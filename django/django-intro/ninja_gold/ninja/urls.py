from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('process_money', views.process_money),
    path('rules',views.rules),
    #Set more specific ones first and more free ones later
    path('<str:location>', views.process_money),
]
