from django import forms
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tasks=["albert","ramos","alin","mariani"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label= "New Task")
    priority =forms.IntegerField (label="Priority", min_value=1, max_value=100)

def index (request):
    # return HttpResponse("This is the Tasks app homepage.")
    return render(request,"tasks/index.html",{
        "tasks":tasks
    })

def add(request):
    return render(request,"tasks/add.html",{
        "form":NewTaskForm
    })