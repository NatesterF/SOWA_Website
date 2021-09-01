from enum import Enum
from django.db import models

class MealTypes(Enum):
    FIRE="Campfire Cooking"
    INDOORS="Indoor Catering"
    SMALL="Small Group Cooking"
# Create your models here.

class Ingredient(models.Model):
    ingredient_name=models.TextField()
    quantity=models.TextField()

class Recipe(models.Model):
    title=models.TextField()
    ingredients_list =  models.ManyToManyField(Ingredient)
    method= models.TextField() #Could be changed to a list (relationship to another table)
    recipe_type=models.CharField(default=MealTypes.INDOORS, max_length=25,choices =[(tag,tag.value) for tag in MealTypes])
