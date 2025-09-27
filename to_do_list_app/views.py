from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Table
from django.http import HttpResponse


# Create your views here.
def index(request):
    mymembers = Table.objects.all().values()
    return render(request,'index.html',{"mymembers": mymembers})
def add(request):
    return render(request,'add.html')
def add_tasks(request):
    ttitle = request.POST['task']
    tstatus = request.POST['status']
    tstatus = request.POST.get('status','pending')
    x=Table(task=ttitle,status=tstatus)
    x.save()
    return redirect('index')


def update(request):
    return render(request,'update.html')

def update_member(request, id):
    member = Table.objects.get (id=id)

    if request.method == "POST":
        member.task = request.POST.get("task")
        member.status = request.POST.get("status")
        # member.status = request.POST.get("status")
        # member.actions = request.POST.get("")
        member.save()
        return redirect("index")
    return render(request, "update.html", {"member": member})

    # if GET, show the form with prefilled values
   
def delete(request):
    return render(request,'delete.html')

def delete_member(request,id):
    member = Table.objects.get (id=id)
    member.delete()
    return redirect("index")












