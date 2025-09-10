from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tasks=["albert","ramos","alin","mariani"]

def index (request):
    # return HttpResponse("This is the Tasks app homepage.")
    return render(request,"tasks/index.html",{
        "tasks":tasks
    })

def add(request):
    return render(request,"tasks/add.html")