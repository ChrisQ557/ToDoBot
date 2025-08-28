from django.core.management.base import BaseCommand
from django.utils import timezone
from todo.models import Task, Notification
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Notify users of their tasks due in the next 12 hours.'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        self.stdout.write(f"Current time: {now}")
        soon = now + timezone.timedelta(hours=12)
        self.stdout.write(f"Notification window ends at: {soon}")
        user_model = get_user_model()
        count = 0

        # Get all user tasks (not automation) due in next 12 hours
        tasks = Task.objects.filter(
            task_type='user',
            is_completed=False,
            scheduled_time__gte=now,
            scheduled_time__lte=soon
        )
        self.stdout.write(f"Found candidate tasks: {tasks.count()}")

        for task in tasks:
            # Check if notification already exists for this task & user within upcoming 12 hours
            recent = Notification.objects.filter(
                user=task.user,
                message__startswith=f"Reminder: Task '{task.title}'",
                created_at__gte=now - timezone.timedelta(hours=1)
            ).exists()
            if recent:
                continue  # Avoid duplicate reminders
            Notification.objects.create(
                user=task.user,
                message=f"Reminder: Task '{task.title}' is due at {task.scheduled_time.strftime('%Y-%m-%d %H:%M')}."
            )
            count += 1
            self.stdout.write(self.style.SUCCESS(f"Notified {task.user} about task '{task.title}' due at {task.scheduled_time}"))
        if count == 0:
            self.stdout.write("No upcoming tasks to notify.")
