# Generated by Django 5.0.2 on 2024-04-25 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontSmart', '0004_task_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='isCompleted',
        ),
    ]