"""bda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from projects.views import landing, about, detail, project_points, map_view, list_view, new_project, edit_project, delete_project


urlpatterns = [
    path('', landing, name='landing'),
    path('about/', about, name='about'),
    path('<int:project_id>', detail, name='detail'),
    path('points.data/', project_points, name='project_points'),
    path('map_view/', map_view, name='map_view'),
    path('list_view/', list_view, name='list_view'),
    path('new_project/', new_project, name='new_project'),
    path('<int:project_id>/edit_project', edit_project, name='edit_project'),
    path('<int:project_id>/delete_project', delete_project, name='delete_project'),
]
