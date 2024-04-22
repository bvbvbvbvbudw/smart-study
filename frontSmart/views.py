from django.shortcuts import render, get_object_or_404
from .models import Task
from django.shortcuts import render, redirect
from frontSmart.forms import AddTaskForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'front/page/index.html')

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
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = AddTaskForm()
    return render(request, 'front/page/taskAdd.html', {'form': form})
    # if request.method == 'POST':
    #     form = AddTaskForm(request.POST)
    #     if form.is_valid():
    #         task = Task(
    #             subject = form.changed_data['subject'],
    #             date = form.changed_data['date'],
    #             task = form.changed_data['task'],
    #             topic = form.changed_data['topic'],
    #             description = form.changed_data['description'],
    #         )
    #         task.save()
    #         return HttpResponseRedirect(f'/tasks/{task.id}')
    # return render(request, 'front/page/taskAdd.html', {'form': AddTaskForm})
