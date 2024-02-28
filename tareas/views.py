from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def tasks(request):
    #busca por usuario y si datecompleted es nulo
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def tasks_completed(request):
    #busca por usuario y si datecompleted no es nulo
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks_completed.html', {"tasks": tasks})
