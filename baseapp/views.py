from django.shortcuts import render,redirect
from .models import Task

# Create your views here.

def index(request):
    return render(request,'index.html')

def addtask(request):
    task=Task.objects.all()
    if request.method=='POST':
        form=Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Task()
    
    
    return render(request,'addtask.html',{'form':form,'task':task})