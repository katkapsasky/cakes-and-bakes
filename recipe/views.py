from django.shortcuts import render
from django.views import generic
from .models import Post


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(approved=True).order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 6
