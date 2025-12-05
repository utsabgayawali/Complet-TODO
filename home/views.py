from django.shortcuts import render,HttpResponse



def home(request):
    return render(request,'home.html')

def task(request):
    return render(request,'task.html')