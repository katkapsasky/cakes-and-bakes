from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    '''
    Database model for recipe categories
    '''
    recipe_type = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.recipe_type


class Recipe(models.Model):
    '''
    Database model for recipe components
    '''
    title = models.CharField(
        max_length=50, unique=True, null=False, blank=False
    )
    slug = models.SlugField(
        max_length=200, unique=True, null=False, blank=False
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_post"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    total_time = models.CharField(max_length=50, null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    method = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    recipe_description = models.CharField(
        max_length=200, null=False, blank=False
    )
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
