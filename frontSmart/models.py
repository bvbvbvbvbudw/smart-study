from django.db import models

# Create your models here.
<<<<<<< HEAD

class Task(models.Model):
    subject = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False)
    task = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
=======
>>>>>>> 09c94878ff8f9f97a241ef29a5cbfd6a72af3c3c
