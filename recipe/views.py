from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Recipe, Category
from .forms import RecipeForm, CategoryForm


class RecipeList(generic.ListView):
    """
    Class based view to create paginated list of
    posted recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(approved=True).order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    Class based view to show recipe details
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(approved=True)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "liked": liked
            },
        )


def post_recipe(request):
    """
    Function to post a new recipe
    """
    recipe_form = RecipeForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if recipe_form.is_valid():
            recipe_form.instance.author = request.user
            recipe_form.save()
            messages.success(
                request,
                'Recipe successfully added and awaiting approval!'
            )
            return redirect('home')

        messages.error(request, 'An error has occurred, please try again.')
    template = 'post_recipe.html'
    context = {
        'recipe_form': recipe_form,
    }
    return render(request, template, context)


def edit_recipe(request, slug):
    """
    Function to edit an existing recipe
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if recipe.author != request.user:
        messages.error(
            request,
            'This is not your recipe, you do not have access to editing.'
        )
        return redirect('home')
    if request.method == "POST":
        recipe_form = RecipeForm(
            request.POST,
            request.FILES,
            instance=recipe,
        )
        if recipe_form.is_valid():
            recipe_form.instance.approved = False
            recipe_form.save()
            messages.success(
                request,
                'Recipe successfully updated and pending approval!'
            )
            return redirect('home')

        messages.error(request, 'An error has occurred, please try again.')
    recipe_form = RecipeForm(instance=recipe)
    template = 'edit_recipe.html'
    context = {
        'recipe_form': recipe_form,
        'recipe': recipe,
    }
    return render(request, template, context)


def delete_recipe(request, slug):
    """
    Function to delete a recipe
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if recipe.author != request.user:
        messages.error(
            request,
            'This is not your recipe, you do not have access to editing.'
        )
        return redirect('home')
    recipe.delete()
    messages.success(
        request,
        'Recipe successfully deleted!'
    )
    return redirect('home')


class RecipeLikes(View):
    """
    Class based function to like a recipe
    """
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
            messages.success(
                request,
                'Recipe successfully unliked.'
            )
        else:
            recipe.likes.add(request.user)
            messages.success(
                request,
                'Recipe successfully liked.'
            )
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def manage_categories(request):
    """
    Manage categories as superuser
    """
    if not request.user.is_superuser:
        # user is not superuser; take to home page
        messages.error(request, 'Access denied. Invalid permissions.')
        return redirect(reverse('home'))
    categories = Category.objects.all().order_by('recipe_type')
    template = 'manage_categories.html'
    context = {
        'categories': categories,
    }
    return render(request, template, context)


def post_category(request):
    """
    Function to post a new category type
    """
    if not request.user.is_superuser:
        # user is not superuser; take to home page
        messages.error(request, 'Access denied. Invalid permissions.')
        return redirect(reverse('home'))
    category_form = CategoryForm(request.POST or None)
    if request.method == "POST":
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category successfully added!')
            return redirect('manage_categories')

        messages.error(request, 'An error has occurred, please try again.')
    template = 'post_category.html'
    context = {
        'category_form': category_form,
    }
    return render(request, template, context)


def edit_category(request, id):
    """
    Function to edit an existing category type
    """
    if not request.user.is_superuser:
        # user is not superuser; take to home page
        messages.error(request, 'Access denied. Invalid permissions.')
        return redirect(reverse('home'))
    category = get_object_or_404(Category, id=id)
    category_form = CategoryForm(request.POST or None, instance=category)
    if request.method == "POST":
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category successfully edited!')
            return redirect('manage_categories')

        messages.error(request, 'An error has occurred, please try again.')
    template = 'edit_category.html'
    context = {
        'category': category,
        'category_form': category_form,
    }
    return render(request, template, context)


def delete_category(request, id):
    """
    Function to delete an existing category type
    """
    if not request.user.is_superuser:
        # user is not superuser; take to home page
        messages.error(request, 'Access denied. Invalid permissions.')
        return redirect(reverse('home'))
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, 'Category successfully deleted!')
    return redirect('manage_categories')


def liked_recipes(request):
    """
    A page dedicated to the user's liked/saved recipes.
    """
    recipes = Recipe.objects.filter(likes=request.user)
    template = 'liked_recipes.html'
    context = {
        'recipes': recipes,
    }
    return render(request, template, context)
