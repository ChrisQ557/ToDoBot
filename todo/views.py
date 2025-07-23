from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Task

# Create your views here
class TaskList(generic.ListView):
    queryset = Task.objects.order_by('user')
    template_name = 'todo/index.html'
    paginate_by = 9

def task_detail(request, slug):
    """
    Display an individual :model:`todo.Task`.

    Context
        task
            An instance of :model:`todo.Task`.

    Template
        todo/task_detail.html
    """
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'todo/task_detail.html', {'task': task})

    
   

