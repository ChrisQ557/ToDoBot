from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    TASK_TYPE_CHOICES = [
        ('user', 'User Task'),
        ('automation', 'Home Automation'),
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES, default='user')
    recurrence_time = models.TimeField(null=True, blank=True, help_text="Time of day for automation task recurrence")
    recurrence_days = models.CharField(max_length=20, blank=True, help_text="Comma-separated days for automation (e.g. 'mon,tue,wed')")
    last_completed_date = models.DateField(null=True, blank=True, help_text="The last date this automation task was completed.")

    def __str__(self):
        return self.title
