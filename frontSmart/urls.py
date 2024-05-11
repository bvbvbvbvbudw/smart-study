from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='index'),
    # path('tasks/', views.tasks),
    path('tasks/<int:taskId>', views.getTask, name='getTask'),
    path('addTask/', views.addTask, name="addTask"),
    path('updateTask/<int:taskId>', views.updateTask, name='updateTask'),
    path('submitTask/<int:taskId>', views.submitTask, name="submitTask"),
    path('tasks/<str:date>/', views.getTaskByDate, name='getTaskByDate'),
]