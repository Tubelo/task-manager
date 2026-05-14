from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('nova/', views.task_create, name='task_create'),
    path('editar/<int:pk>/', views.task_edit, name='task_edit'),
    path('excluir/<int:pk>/', views.task_delete, name='task_delete'),
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]