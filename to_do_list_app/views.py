from django.shortcuts import render
from django.shortcuts import redirect, render,get_object_or_404
from .models import Table
from django.http import HttpResponse


# Create your views here.
def index(request):
    mytasks = Table.objects.all().values()
    return render(request,'index.html',{"mytasks": mytasks})

def add(request):
    return render(request,'add.html')
def add_tasks(request):
    task = request.POST['task']
    status = request.POST['status']
    status = request.POST.get('status','pending')
    due_date = request.POST.get("due_date")
    x=Table(task=task,status=status,due_date=due_date)
    x.save()
    return redirect('index')

def update(request):
    return render(request,'update.html')

def update_tasks(request, id):
    tasks = Table.objects.get (id=id)

    if request.method == "POST":
        tasks.task = request.POST.get("task")
        tasks.status = request.POST.get("status")
        tasks.due_date = request.POST.get("due_date")
        tasks.save()
        return redirect("index")
    return render(request, "update.html", {"tasks": tasks})


def delete(request, id):
    task = get_object_or_404(Table, id=id)
    if request.method == "POST":
        task.delete()
        return redirect("index")
    return render(request, "delete.html", {"mytasks": task}) 

def delete_tasks(request,id):
    tasks = Table.objects.get (id=id)
    tasks.delete()
    return redirect("delete")














