import json
from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import GEOSGeometry

from .models import Project

# Create your views here.


def landing(request):
    return render(request, 'projects/landing.html')


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project})


def project_points(request):
        projects_as_geojson = serialize('geojson', Project.objects.all())
        return JsonResponse(json.loads(projects_as_geojson))


def map_view(request):
    return render(request, 'projects/map_view.html')


def list_view(request):
    projects = Project.objects.all()
    return render(request, 'projects/list_view.html', {'projects': projects})

# CRUD views


@login_required(login_url="/landing")
def new_project(request):
    if request.method == 'POST':
        project = Project()
        project.ProjectName = request.POST['ProjectName']
        project.StreamName = request.POST['StreamName']
        project.BasinName = request.POST['BasinName']
        project.ProjectLatitude = request.POST['ProjectLatitude']
        project.ProjectLongitude = request.POST['ProjectLongitude']
        project.CreatedBy = request.user
        project.ProjectImage = request.FILES['ProjectImage']
        project.ProjectAffiliation = request.POST['ProjectAffiliation']

        lon = request.POST['ProjectLongitude']
        lat = request.POST['ProjectLatitude']
        project.geom = GEOSGeometry('POINT(' + lon + ' ' + lat + ')')
        project.save()
        return redirect('landing')
    else:
        return render(request, 'projects/new_project.html')
