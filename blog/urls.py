from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),  # Home page for listing recipes
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),  # Detail page for a single recipe
    path('recipe/new/', views.recipe_create, name='recipe_create'),  # Page for creating a new recipe
    path('recipe/<int:pk>/edit/', views.recipe_update, name='recipe_update'),  # Page for editing a recipe
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),  # Page for deleting a recipe
]