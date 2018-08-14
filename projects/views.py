import json
from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.serializers import serialize
from django.http import JsonResponse

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
