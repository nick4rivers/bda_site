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
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('<int:project_id>', views.detail, name='detail'),
    path('points.data/', views.project_points, name='project_points'),
    path('map_view/', views.map_view, name='map_view'),
    path('list_view/', views.list_view, name='list_view'),
    path('new_project/', views.new_project, name='new_project'),
]
