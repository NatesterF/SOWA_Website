from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredient_name=models.TextField()
    quantity=models.TextField()

class Recipe(models.Model):
    title=models.TextField()
    ingredients_list =  models.ManyToManyField(Ingredient)
    method= models.TextField() #Could be changed to a list (relationship to another table)
