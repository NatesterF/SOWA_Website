from django.shortcuts import render, get_object_or_404
from django.http import *
from .models import *

# Create your views here.
def index(request):
    return render(request, "recipes/recipe.html")
    #return HttpResponse("Hello,World")
def getRecipe(request,recipe_name):
    info = Recipe.objects.raw(f"SELECT * From recipes_recipe WHERE url_name='{recipe_name}'")[-1]
    return render(request,"recipes/recipe.html",{'recipe':info})

def recipesOfType(request,cooking_type="all"):
    if cooking_type == "all":
        recipe_list = Recipe.objects.raw(f"SELECT * From recipes_recipe")
    else:
        recipe_list = Recipe.objects.raw(f"SELECT * From recipes_recipe WHERE recipe_type='{cooking_type}'")
    return render(request,"recipes/recipelist.html",{'recipe_list':recipe_list})

