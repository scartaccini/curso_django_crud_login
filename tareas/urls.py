from django.urls import path
from tareas import views

urlpatterns = [
path('tasks/', views.tasks, name='tasks'),
path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
path('create_task/', views.create_task, name='create_task'),
path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
path('taks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]

