from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post"
    )
    total_time = models.CharField(max_length=50)
    method = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    recipe_description = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True
    )
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Ingredient(models.Model):
    recipe_name = models.ForeignKey(
        Recipe, related_name='ingredients', on_delete=models.CASCADE
    )
    ingredient_name = models.CharField(max_length=50)
    metric = models.CharField(max_length=25)
    quantity = models.IntegerField()


class Category(models.Model):
    recipe_type = models.CharField(max_length=50)
