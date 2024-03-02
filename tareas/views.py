from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.utils import timezone

######LISTAR######
@login_required
def tareas_pendientes(request):
    #busca por usuario y si datecompleted es nulo
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'lista_tareas.html', {"tasks": tasks,"pendientes":"TAREAS PENDIENTES"})

@login_required
def tareas_completadas(request):
    #busca por usuario y si datecompleted no es nulo
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'lista_tareas.html', {"tasks": tasks,"realizadas":"TAREAS COMPLETADAS"})

######LISTAR######

######CREAR######

@login_required
def crear_tarea(request):
    if request.method == "GET":
        return render(request, 'crea_tarea.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tareas_pendientes')
        except ValueError:
            return render(request, 'crea_tarea.html', {"form": TaskForm, "error": "Error creating task."})
        
######CREAR######

######ACTUALIZAR######
        
@login_required
def opciones_tarea(request, task_id):
    if request.method == 'GET':
        #task = get_object_or_404(Task, pk=task_id)
        task = get_object_or_404(Task, pk=task_id, user=request.user) #busca tarea por id y por usuario
        form = TaskForm(instance=task)
        return render(request, 'opciones_tareas.html', {'task':task, 'form': form})
    else:
        try:
            #task = get_object_or_404(Task, pk=task_id)
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tareas_pendientes')
        except ValueError:
            return render(request, 'opciones_tareas.html', {'task':task, 'form': form, 'error': 'Error updating task.'})
        
#mejor opcion usar get_object_or_404       
'''def opciones_tarea(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        return render(request, 'opciones_tareas.html',{'form':task})
    except:
        return render(request,'opciones_tareas.html',{'form':'NO existe'})'''
        
        
@login_required
def marcar_tarea_completada(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tareas_pendientes')

######ACTUALIZAR######

######ELIMINAR######

@login_required
def eliminar_tarea(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tareas_pendientes')
        
######ELIMINAR######

