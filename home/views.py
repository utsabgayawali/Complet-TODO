from django.shortcuts import render,HttpResponse
from .models import Todo



def home(request):
    if request.method == 'POST':
        task_name= request.POST.get('task_name')
        description = request.POST.get('description')
        todo= Todo(task_name=task_name,description=description)
        todo.save()
    return render(request,'home.html')

def task(request):
    task = Todo.objects.all()
    return render(request,'task.html',  context={'task_item':task})