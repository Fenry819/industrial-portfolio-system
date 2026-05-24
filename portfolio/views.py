from django.shortcuts import render
from .models import Project

def home(request):
    # Fetch all projects ordered according to your custom positioning
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})