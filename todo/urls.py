from . import views
from django.urls import path


urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('<slug:slug>/', views.task_detail, name='task_detail'),
]