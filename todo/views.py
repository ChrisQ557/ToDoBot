from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm

# Create your views here
class TaskList(LoginRequiredMixin, generic.ListView):
    template_name = 'todo/index.html'
    paginate_by = 6

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

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

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            from django.utils.text import slugify
            task.slug = slugify(task.title)
            task.save()
            from django.urls import reverse
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect(reverse('task_detail', args=[task.slug]))
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})

@login_required
def delete_task(request, slug):
    task = get_object_or_404(Task, slug=slug, user=request.user)
    if request.method == 'POST':
        task.delete()
        from django.urls import reverse
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

    
   

