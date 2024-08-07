from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from datetime import datetime
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task

# Create your views here.
def home(request):
    return render(request,'home.html')

def tasks(request):
    today = datetime.today()
    print(today.hour)
    tasks = Task.objects.all().order_by('tiex','diasanotados','datecontra','id')#filter(user=request.user)  #se deja como all() para obtener la informacion de todos los usuarios
    for task in tasks:
        if (task.datecontra.month-today.month) >= 0 and (task.datecontra.day-today.day) >= 0:
            task.anotado = True
        else:
            task.anotado = False
    return render(request,'tasks.html',{
        'tasks':tasks,
        'today' : today,
    })

def orden(request):
    today = datetime.today()
    tasks = Task.objects.all().order_by('tiex','diasanotados','datecontra','id')#filter(user=request.user)  #se deja como all() para obtener la informacion de todos los usuarios
    for task in tasks:
        if (task.datecontra.month-today.month) >= 0 and (task.datecontra.day-today.day) >= 0:
            task.anotado = True
        else:
            task.anotado = False
    return render(request,'orden.html',{
        'tasks':tasks,
        'today' : today,
    })

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],
                                           password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
                'form':AuthenticationForm,
                'error':'Usuario o contraseña incorrectos'})
        else:
            login(request,user)
            return redirect('orden')  
        
def signout(request):
    logout(request)
    return redirect('home')

def task_detail(request,task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task,pk=task_id,user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html',
                  {'task':task,
                   'form':form})
    else:
        try:
            task = get_object_or_404(Task,pk=task_id,user=request.user)
            form =TaskForm(request.POST,instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html',
                  {'task':task,
                   'form':form,
                   'error':'Error actualizando datos'})
