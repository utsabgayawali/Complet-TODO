from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Todo
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        task_name= request.POST.get('task_name')
        description = request.POST.get('description')
        todo= Todo(task_name=task_name,description=description)
        todo.save()
        messages.success(request,'Your task is added sucessfully !!')
        return redirect('home')
        
    return render(request,'home.html')

def task(request):
    task = Todo.objects.all()
    return render(request,'task.html',  context={'task_item':task})


         

def delete(request,task_id):
    task = get_object_or_404(Todo, pk=task_id)
    task.delete()
    return redirect('task')
