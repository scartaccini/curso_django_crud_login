from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.utils import timezone

@login_required
def tasks(request):
    #busca por usuario y si datecompleted es nulo
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def tasks_completed(request):
    #busca por usuario y si datecompleted no es nulo
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})
        
#mejor opcion usar get_object_or_404       
'''def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        return render(request, 'task_detail.html',{'form':task})
    except:
        return render(request,'task_detail.html',{'form':'NO existe'})'''       


@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        #task = get_object_or_404(Task, pk=task_id)
        task = get_object_or_404(Task, pk=task_id, user=request.user) #busca tarea por id y por usuario
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task':task, 'form': form})
    else:
        try:
            #task = get_object_or_404(Task, pk=task_id)
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task':task, 'form': form, 'error': 'Error updating task.'})
        
        
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
        

