from django.shortcuts import render, get_object_or_404
from .models import Task
from django.shortcuts import render, redirect
from frontSmart.forms import AddTaskForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'front/page/index.html', {'taskList': tasks})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'front/page/index.html', {'taskList': tasks})

def getTask(request, taskId):
    task = get_object_or_404(Task, pk=taskId)
    return render(request, 'front/page/task.html', {'task': task})

def addTask(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('index')
    else:
        form = AddTaskForm()
    return render(request, 'front/page/taskAdd.html', {'form': form})
