from django.shortcuts import render,redirect,get_object_or_404
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
            return redirect('listtask')
    else:
        form = Taskform()
    
    
    return render(request,'addtask.html',{'form':form,'task':task})

def listtask(request):
    tasks = Task.objects.filter(is_completed=False)
    return render(request, 'listtask.html', {'tasks': tasks})
def completedtask(request):
    tasks = Task.objects.filter(is_completed=True)
    return render(request, 'completedtask.html', {'tasks': tasks})


def taskdetails(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskdetails.html', {'task': task})

def completetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_completed = True
        task.save()
        return redirect('listtask')
    return redirect('listtask')