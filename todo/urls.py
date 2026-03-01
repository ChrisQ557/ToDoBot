from . import views
from django.urls import path


urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('create/', views.create_task, name='create_task'),
    path(
        '<slug:slug>/delete/',
        views.delete_task, name='delete_task'
    ),
    path(
        '<slug:slug>/',
        views.task_detail, name='task_detail'
    ),
    path(
        'notifications/clear/',
        views.clear_notifications,
        name='clear_notifications'
    ),
]
