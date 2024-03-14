<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Task
=======
from django.shortcuts import render
>>>>>>> 09c94878ff8f9f97a241ef29a5cbfd6a72af3c3c

# Create your views here.
def index(request):
    return render(request, 'front/page/index.html')
<<<<<<< HEAD


def Tasks(request):
    tasks = Task.objects.all()
    return render(request, 'front/page/index.html', {'taskList': tasks})
=======
>>>>>>> 09c94878ff8f9f97a241ef29a5cbfd6a72af3c3c
