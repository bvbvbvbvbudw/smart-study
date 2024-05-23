from django import forms
from frontSmart.models import Task


class TaskForm(forms.ModelForm):
    subject = forms.CharField(max_length=255)
    date = forms.DateField()
    task = forms.CharField(max_length=255)
    topic = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)

    class Meta:
        model = Task
        exclude = ['file','isCompleted','completedTask']



class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['isCompleted', 'completedTask']



class SubmitForm(forms.ModelForm):
    completedTask = forms.FileField()
    isCompleted = True

    class Meta:
        model = Task
        exclude = ['file','subject','date','task','topic','description']