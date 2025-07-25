from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Task
from .forms import TaskForm

# Create your views here
class TaskList(generic.ListView):
    queryset = Task.objects.order_by('user')
    template_name = 'todo/index.html'
    paginate_by = 9

@login_required
def task_detail(request, slug):
    """
    Display an individual :model:`todo.Task` and its form.

    Context
        task
            An instance of :model:`todo.Task`.
        form
            A form instance for :model:`todo.Task`.

    Template
        todo/task_detail.html
    """
    task = get_object_or_404(Task, slug=slug, user=request.user)
    form = TaskForm(instance=task)
    return render(
        request,
        "todo/task_detail.html",
        {
            "task": task,
            "form": form,
        },
    )

    
   

