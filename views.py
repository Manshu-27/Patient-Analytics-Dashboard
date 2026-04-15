from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')