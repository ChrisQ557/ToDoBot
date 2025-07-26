from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'category',
            'scheduled_time',
            'is_completed',
            'task_type',
            'recurrence_time',
            'recurrence_days',
        ]
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'recurrence_time': forms.TimeInput(attrs={'type': 'time'}),
        }