from django.contrib import admin
from .models import Task, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "user", "category", "is_completed", "slug")
    search_fields = ("title", "description", "slug")
    summernote_fields = ('description',)
   


#Register your models here.
admin.site.register(Category)
