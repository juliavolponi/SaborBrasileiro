"""
URL configuration for sabor_brasileiro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from .views import recipe_list, recipe_detail, recipe_create, recipe_update, recipe_delete

urlpatterns = [
   path('', recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/new/', recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', recipe_update, name='recipe_update'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
]
