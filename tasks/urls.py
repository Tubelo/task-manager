from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('nova/', views.task_create, name='task_create'),
]