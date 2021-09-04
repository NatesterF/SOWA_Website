from django import forms
from django.forms import ModelForm
from django.db import models
from .models import MealLog
import datetime

class MealForm(ModelForm):
    class Meta:
        model = MealLog
        fields = ['group_name','meal_eaten','date','how_did_you_find_it']


