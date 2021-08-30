from django.db import models

# Create your models here.

class Recipe(models.Model):
    title=models.TextField()
    ingredients_list =  models.ManyTOManyField(Ingredient)
    method= models.TextField() #Could be changed to a list (relationship to another table)
class Ingredient(models.Models):
    ingredient_name=models.TextField():
    quantity=models.TextField()
