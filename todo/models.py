from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    is_recurring = models.BooleanField(default=False)
    recurrence_pattern = models.CharField(max_length=255, blank=True)
    task_type = models.CharField(max_length=100, blank=True)
    device_type = models.CharField(max_length=100, blank=True)
    action = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
