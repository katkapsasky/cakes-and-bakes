from django.contrib import admin
from .models import Recipe, Category


class RecipeAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'approved', 'posted_on')
    search_fields = ['title', 'author']
    list_filter = ('approved', 'posted_on')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('recipe_type',)}


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
