from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {"tasks" : tasks,"form":form}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'tasks/list.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"form":form}
    return render(request, "tasks/update.html",context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {"item":item}
    return render(request, 'tasks/delete.html',context)