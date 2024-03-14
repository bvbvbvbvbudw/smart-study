from django.shortcuts import render, get_object_or_404
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'front/page/index.html')


def Tasks(request):
    tasks = Task.objects.all()
    return render(request, 'front/page/index.html', {'taskList': tasks})
