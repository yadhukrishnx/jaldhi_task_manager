from django.shortcuts import render,redirect
from .models import Task
from .forms import Taskform

# Create your views here.

def index(request):
    return render(request,'index.html')

def addtask(request):
    task=Task.objects.all()
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Taskform()
    
    
    return render(request,'addtask.html',{'form':form,'task':task})

def listtask(request):
    tasks = Task.objects.all()
    return render(request, 'listtask.html', {'tasks': tasks})