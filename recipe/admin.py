from django.contrib import admin
from .models import Recipe, Category


class RecipeAdmin(admin.ModelAdmin):
    '''
    Class based function to display recipe posts
    and allow admin to search through and approve posted recipes
    '''
    list_display = ('title', 'slug', 'approved', 'posted_on')
    search_fields = ['title', 'author']
    list_filter = ('approved', 'posted_on')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
