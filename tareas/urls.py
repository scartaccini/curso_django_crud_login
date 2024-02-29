from django.urls import path
from tareas import views

urlpatterns = [
path('tasks/', views.tasks, name='tasks'),
path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
path('create_task/', views.create_task, name='create_task'),
]

