from django.shortcuts import render
from .models import Project

# Create your views here.


def project_test(request):
    projects = Project.objects
    return render(request, 'projects/base.html', {'projects': projects})
