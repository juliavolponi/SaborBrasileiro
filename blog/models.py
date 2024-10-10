from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=250)
    ingredients = models.TextField()
    cooking_method = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # comments are deleted as well if a post is deleted
    categories = models.ManyToManyField(Category, related_name="recipes")  # Many-to-Many relationship
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
