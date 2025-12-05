from django.shortcuts import render,HttpResponse



def home(request):
    return render(request,'home.html')

def content(request):
    return render(request,'content.html')