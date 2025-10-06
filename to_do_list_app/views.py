from django.shortcuts import render
from django.shortcuts import redirect, render,get_object_or_404
from .models import Table
from django.http import HttpResponse
from datetime import date


def index(request):
    mytasks = Table.objects.all().values()
    today = date.today()
    return render(request,'index.html',{"mytasks": mytasks,"today": today})

def add(request):
    today = date.today()
    return render(request,'add.html',{"today": today})

def add_tasks(request):
    task = request.POST['task']
    status = request.POST['status']
    status = request.POST.get('status','pending')
    due_date = request.POST.get("due_date")

    x=Table(task=task,status=status,due_date=due_date)
    x.save()
    return redirect('index')

# def update(request):
#     return render(request,'update.html')

def update_tasks(request, id):
    tasks = Table.objects.get (id=id)

    if request.method == "POST":
        new_due_date= request.POST.get("due_date")
        if new_due_date and new_due_date < str(date.today()):
            return HttpResponse("Error: Due date cannot be in the past!")
        tasks.task = request.POST.get("task")
        tasks.status = request.POST.get("status")
        tasks.due_date = new_due_date
        tasks.save()
        return redirect("index")
    today = date.today()
    return render(request, "update.html", {"tasks": tasks,"today":today})


def delete(request, id):
    task = get_object_or_404(Table, id=id)
    if request.method == "POST":
        task.delete()
        return redirect("index")
    return render(request, "delete.html", {"mytasks": task}) 

# def delete_tasks(request,id):
#     tasks = Table.objects.get (id=id)
#     tasks.delete()
#     return redirect("delete")















