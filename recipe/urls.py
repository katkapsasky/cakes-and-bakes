from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('post_recipe/', views.post_recipe, name='post_recipe'),
    path('edit_recipe/<slug:slug>/', views.edit_recipe, name='edit_recipe'),
    path('post_category/', views.post_category, name='post_category'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
