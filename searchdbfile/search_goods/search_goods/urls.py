"""
URL configuration for search_goods project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from . import views
from .views import upload_image  # make sure to import your view function

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.search, name = 'search'),
    path('search/', views.search_results, name='search_results'),
    #path('', lambda request: redirect('search_results')), 
    path('upload-image/', upload_image, name='upload_image')
    #path('upload-image/', upload_image, name='upload_image')
]


