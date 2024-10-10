from django.urls import path
from .views import recipe_list, recipe_detail, recipe_create, recipe_update, recipe_delete

urlpatterns = [
    path('', recipe_list, name='recipe_list'),  # Home page for listing recipes
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),  # Detail page for a single recipe
    path('recipe/new/', recipe_create, name='recipe_create'),  # Page for creating a new recipe
    path('recipe/<int:pk>/edit/', recipe_update, name='recipe_update'),  # Page for editing a recipe
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),  # Page for deleting a recipe
]