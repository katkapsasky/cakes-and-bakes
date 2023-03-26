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


class RecipeAdminSite(admin.AdminSite):
    '''
    Class based function to create additional admin site
    for site administrators/managers
    '''
    site_header = "Recipe Post Admin"
    site_title = "Recipe Post Admin Portal"
    title = "Welcome to Cakes & Bakes"


recipe_admin_site = RecipeAdminSite(name='recipe_admin')


recipe_admin_site.register(Recipe)
recipe_admin_site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
