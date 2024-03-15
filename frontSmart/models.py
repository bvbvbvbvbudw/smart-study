from django.db import models

# Create your models here.

class Task(models.Model):
    subject = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False)
    task = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    description = models.CharField(max_length=255)