from django.db import models
import datetime

# Create your models here.
class MealLog(models.Model):
    group_name = models.CharField( max_length=100)
    meal_eaten=models.CharField(max_length=100)
    date=models.DateField(default=datetime.date.today)
    how_did_you_find_it=models.TextField()
class LeaderboardModel(models.Model):
    group_name = models.CharField( max_length=100)
    meals_eaten=models.IntegerField()
