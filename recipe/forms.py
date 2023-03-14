from .models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'total_time',
            'ingredient_name',
            'metric',
            'quantity',
            'method',
            'image',
            'recipe_description',
        )
