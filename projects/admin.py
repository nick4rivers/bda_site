from django.contrib import admin
from .models import Project
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

admin.site.register(Project, LeafletGeoAdmin)
