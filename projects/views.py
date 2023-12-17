from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

# Create your views here.

def projects_list(request):

    projects = Project.objects.all()

    return render(request, 'projects/list.html', {
        'projects': projects
    })

def project_new(request):
    form = ProjectForm()

    return render(request, 'projects/new.html', {
        'form': form
    })