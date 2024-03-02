from django.urls import path
from tareas import views

urlpatterns = [
path('tareas_pendientes/', views.tareas_pendientes, name='tareas_pendientes'),
path('tareas_completadas/', views.tareas_completadas, name='tareas_completadas'),
path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
path('opciones_tarea/<int:task_id>', views.opciones_tarea, name='opciones_tarea'),
path('marcar_tarea_completada/<int:task_id>/', views.marcar_tarea_completada, name='marcar_tarea_completada'),
path('eliminar_tarea/<int:task_id>/', views.eliminar_tarea, name='eliminar_tarea'),
]

