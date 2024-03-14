from django.contrib import admin
from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Tasks, name='index'),
]
=======
urlpatterns = [
    path('', views.index, name='index'),
]
>>>>>>> 09c94878ff8f9f97a241ef29a5cbfd6a72af3c3c
