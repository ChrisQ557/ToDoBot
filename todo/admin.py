from django.contrib import admin
from .models import Task, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "user", "category", "is_completed", "slug", "task_type", "recurrence_time", "recurrence_days")
    search_fields = ("title", "description", "slug")
    summernote_fields = ('description',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'user', 'category', 'description', 'scheduled_time', 'is_completed', 'task_type', 'recurrence_time', 'recurrence_days')
        }),
    )

#Register your models here.
admin.site.register(Category)
