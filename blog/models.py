from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, null=True, unique=True, blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # comments are deleted as well if a post is deleted
    categories = models.ManyToManyField(Category, related_name="recipes")  # Many-to-Many relationship
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

