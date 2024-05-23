from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from frontSmart.forms import *
from django.http import HttpResponseRedirect, JsonResponse


def index(request):
    tasks = Task.objects.all()
    return render(request, 'front/page/index.html', {'taskList': tasks})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'front/page/index.html', {'taskList': tasks})

def getTask(request, taskId):
    task = get_object_or_404(Task, pk=taskId)
    return render(request, 'front/page/task.html', {'task': task, 'id': taskId})

def addTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'front/page/taskAdd.html', {'form': form})

def updateTask(request, taskId):
    task = get_object_or_404(Task, pk=taskId)   

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        form.save()
        return redirect('index')
    
    return render(request, 'front/page/taskUpdate.html', {'form': TaskForm(None, instance=task), 'id': taskId})

def getTaskByDate(request, date):
    tasks = Task.objects.filter(date=date)
    tasks_data = [{'id': task.pk, 'task': task.task, 'subject': task.subject} for task in tasks]
    return JsonResponse({'tasks': tasks_data})

def submitTask(request, taskId):
    task = get_object_or_404(Task, pk=taskId)

    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.isCompleted = True
            task.save()
            return redirect('index')
    else:
        form = SubmitForm(instance=task)
    return render(request, 'front/page/task.html', {'form': form, 'task': task})