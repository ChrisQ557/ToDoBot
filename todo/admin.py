from django.contrib import admin
from .models import Task, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):

    list_display = ('title', 'is_completed', 'created_at')
    search_fields = ['title']
    summernote_fields = ('description',)
   


#Register your models here.
admin.site.register(Category)
