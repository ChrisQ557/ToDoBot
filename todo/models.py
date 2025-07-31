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

    @property
    def is_overdue(self):
        from django.utils import timezone
        return (
            self.scheduled_time is not None and
            self.scheduled_time < timezone.now() and
            not self.is_completed and
            self.task_type != 'automation'
        )

    @property
    def is_due_soon(self):
        from django.utils import timezone
        if self.scheduled_time is None or self.is_completed or self.task_type == 'automation':
            return False
        now = timezone.now()
        soon = now + timezone.timedelta(hours=24)
        return now <= self.scheduled_time <= soon

    @property
    def is_pending(self):
        return not self.is_completed and not self.is_overdue and self.task_type != 'automation'

    @property
    def is_pending_for_today(self):
        from django.utils import timezone
        if self.task_type != 'automation':
            return False
        today = timezone.localdate()
        # Check recurrence_days
        if self.recurrence_days:
            days = [d.strip().lower() for d in self.recurrence_days.split(',') if d.strip()]
            weekday = today.strftime('%a').lower()[:3]  # e.g. 'mon', 'tue'
            if weekday not in days:
                return False
        # Check recurrence_time (optional)
        if self.recurrence_time:
            now_time = timezone.localtime().time()
            if now_time < self.recurrence_time:
                return False
        # Check if already completed today
        return self.last_completed_date != today

class Notification(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user}: {self.message}"
