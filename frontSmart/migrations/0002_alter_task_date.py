# Generated by Django 5.0.2 on 2024-03-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontSmart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
