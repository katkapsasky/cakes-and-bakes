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
    ingredient_name = models.CharField(max_length=50, null=True)
    metric = models.CharField(max_length=25, null=True)
    quantity = models.IntegerField(null=True)
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


class Category(models.Model):
    recipe_type = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(u'Description', blank=True, null=True)

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    def __unicode__(self):
        return self.name
