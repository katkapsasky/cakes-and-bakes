from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm, CategoryForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(approved=True).order_by('-posted_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

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

