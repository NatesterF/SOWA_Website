from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.recipesOfType, name='Recipes of certain type'),
    path('<recipe_name>', views.getRecipe, name='recipe'),
    path('list/<cooking_type>', views.recipesOfType, name='Recipes of certain type'),
]
