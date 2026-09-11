from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm


def home(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    search = request.GET.get('search', '')

    tasks = Task.objects.all().order_by('-created_at')

    if search:
        tasks = tasks.filter(title__icontains=search)

    return render(request, 'tasks/home.html', {
        'tasks': tasks,
        'form': form,
        'search': search
    })


def toggle_task(request, id):

    task = get_object_or_404(Task, id=id)

    task.completed = not task.completed
    task.save()

    return redirect('home')


def delete_task(request, id):

    task = get_object_or_404(Task, id=id)

    task.delete()

    return redirect('home')


def task_api(request):

    completed = request.GET.get('completed')

    tasks = Task.objects.all()

    if completed == 'true':
        tasks = tasks.filter(completed=True)

    elif completed == 'false':
        tasks = tasks.filter(completed=False)

    data = list(tasks.values(
        'id',
        'title',
        'completed',
        'created_at'
    ))

    return JsonResponse(data, safe=False)