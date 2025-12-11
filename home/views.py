from django.shortcuts import render,HttpResponse
from .models import Todo



def home(request):
    return render(request,'home.html')

def task(request):
    task = Todo.objects.all()
    return render(request,'task.html',  context={'task_item':task})