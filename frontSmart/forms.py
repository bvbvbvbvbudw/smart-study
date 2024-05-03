from django import forms
from frontSmart.models import Task


class AddTaskForm(forms.ModelForm):
    subject = forms.CharField(max_length=255)
    date = forms.DateField()
    task = forms.CharField(max_length=255)
    topic = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)

    class Meta:
        model = Task
        exclude = ['file','isCompleted']