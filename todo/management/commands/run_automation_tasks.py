from django.core.management.base import BaseCommand
from todo.models import Task
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Run scheduled home automation tasks and mark them as completed for today.'

    def handle(self, *args, **options):
        now = timezone.localtime()
        today = now.date()
        current_time = now.time().replace(second=0, microsecond=0)
        current_day = now.strftime('%a').lower()[:3]  # e.g., 'mon', 'tue', ...

        tasks = Task.objects.filter(
            task_type='automation',
            recurrence_time__isnull=False,
            recurrence_days__icontains=current_day
        )

        count = 0
        for task in tasks:
            # Check if the recurrence_time matches the current time (to the minute)
            if task.recurrence_time and task.recurrence_time.replace(second=0, microsecond=0) == current_time:
                if task.last_completed_date != today:
                    task.last_completed_date = today
                    task.save(update_fields=['last_completed_date'])
                    self.stdout.write(self.style.SUCCESS(f"Automation task '{task.title}' marked as completed for today."))
                    count += 1
        if count == 0:
            self.stdout.write("No automation tasks to run at this time.")
