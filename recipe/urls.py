from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('post_recipe/', views.post_recipe, name='post_recipe'),
    path('edit_recipe/<slug:slug>/', views.edit_recipe, name='edit_recipe'),
    path('liked_recipes/', views.liked_recipes, name='liked_recipes'),
    path(
        'manage_categories/',
        views.manage_categories,
        name='manage_categories'
    ),
    path('post_category/', views.post_category, name='post_category'),
    path('edit_category/<int:id>/', views.edit_category, name='edit_category'),
    path(
        'delete_category/<int:id>/',
        views.delete_category,
        name='delete_category'
    ),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path(
        'delete_recipe/<slug:slug>/',
        views.delete_recipe,
        name='delete_recipe'
    ),
    path(
        'likes/<slug:slug>',
        views.RecipeLikes.as_view(),
        name='recipe_likes'
    ),
]
