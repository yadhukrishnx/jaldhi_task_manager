from django.shortcuts import render,redirect,get_object_or_404
from .models import Task,UserProfile
from .forms import Taskform,ProfileForm,ImageUploadForm
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')

    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')       
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('register')


def profile(request):
    user_profile = UserProfile.objects.first()  
    return render(request, 'viewprofile.html', {'user_profile': user_profile})

def editprofile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)
        image_form = ImageUploadForm(request.POST, request.FILES, instance=user_profile)
        
        if profile_form.is_valid() and image_form.is_valid():
            profile_form.save()
            image_form.save()
            return redirect('profile')  # Redirect to the view profile page after saving
    else:
        profile_form = ProfileForm(instance=request.user)
        image_form = ImageUploadForm(instance=user_profile)
    
    return render(request, 'editprofile.html', {'profile_form': profile_form, 'image_form': image_form})

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
    paginator=Paginator(tasks,10)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(paginator.num_pages)
        
    
   
    return render(request, 'listtask.html', {'tasks': tasks,'page':page})
def completedtask(request):
    tasks = Task.objects.filter(is_completed=True)
    paginator=Paginator(tasks,10)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(paginator.num_pages)
    return render(request, 'completedtask.html', {'tasks': tasks,'page':page})


def taskdetails(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskdetails.html', {'task': task})

def completetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_completed = not task.is_completed  # Toggle the value
        task.save()
        return redirect('listtask')
    return redirect('listtask')

def deletetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'deletetask.html', {'task': task})

def confirmdelete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('completedtask')
    return redirect('completedtask')

def searchtask(request):
    query=None
    tasks=None
    not_found_message=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        tasks=Task.objects.filter(Q(title__icontains=query))
    else:
        tasks=[]
    if not tasks:
        not_found_message="No Task Found"
        
    return render(request,'searchtask.html',{'query':query,'tasks':tasks,'not_found_message':not_found_message})





def viewprofile(request):

    return render(request, 'viewprofile.html')