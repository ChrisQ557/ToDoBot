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
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'task_type': forms.Select(attrs={'class': 'form-select'}),
            'recurrence_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'recurrence_days': forms.TextInput(attrs={'class': 'form-control'}),
        }