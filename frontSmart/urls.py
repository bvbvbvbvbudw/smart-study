from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Tasks, name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
]

