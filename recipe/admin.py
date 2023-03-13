from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'approved', 'posted_on')
    search_fields = ['title', 'author']
    list_filter = ('approved', 'posted_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('method')
