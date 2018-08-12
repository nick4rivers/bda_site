from django.shortcuts import render, get_object_or_404
from .models import Project


# Create your views here.


def landing(request):
    return render(request, 'projects/landing.html')


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})
