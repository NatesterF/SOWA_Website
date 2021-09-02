from enum import Enum
from django.db import models

class MealTypes(Enum):
    FIRE="Campfire Cooking"
    INDOORS="Indoor Catering"
    SMALL="Small Group Cooking"
    @classmethod
    def all(self):
        return [MealTypes.FIRE,MealTypes.INDOORS,MealTypes.SMALL]
# Create your models here.

class Recipe(models.Model):
    title=models.TextField()
    ingredients_list =  models.TextField(default="")
    method= models.TextField() #Could be changed to a list (relationship to another table)
    recipe_type=models.CharField(max_length=25,choices =[(tag.name,tag.value) for tag in MealTypes.all()])
    url_name=models.TextField(default="", max_length=40)
