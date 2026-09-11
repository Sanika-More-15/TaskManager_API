from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('toggle/<int:id>/', views.toggle_task, name='toggle'),

    path('delete/<int:id>/', views.delete_task, name='delete'),

    path('api/tasks/', views.task_api, name='task_api'),
]