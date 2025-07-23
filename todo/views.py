from django.shortcuts import render
from django.views import generic
from .models import Task

# Create your views here
class TaskList(generic.ListView):
    queryset = Task.objects.order_by('user')
    template_name = 'todo/index.html'
    paginate_by = 9

    
   

