from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(owner=request.user) if request.user.is_authenticated else []
    return render(request, 'tasks/task_list.html', {'tasks': tasks})