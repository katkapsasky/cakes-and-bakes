from django import forms
from .models import Recipe, Category


class CategoryForm(forms.ModelForm):
    '''
    Form for adding new categories
    '''
    class Meta:
        model = Category
        fields = "__all__"


class RecipeForm(forms.ModelForm):
    '''
    Form for posting new recipe
    '''
    class Meta:
        model = Recipe
        fields = "__all__"
        exclude = (
            "author",
            "posted_on",
            "likes",
            "approved",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["slug"].widget = forms.HiddenInput()
