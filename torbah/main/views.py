from django.shortcuts import render
from django.http import HttpResponse
from .models import Farm
from .forms import CreateNewList
# Create your views here.

def index(response):
    # ls = Farm.objects.get(id=id)
    return render(response, "main/home.html", {})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Farm(name=n)
            t.save()
            response.user.todolist.add(t)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def about(response):
    return render(response, "main/about.html", {})

def contact(response):
    return render(response, "main/contact.html", {})