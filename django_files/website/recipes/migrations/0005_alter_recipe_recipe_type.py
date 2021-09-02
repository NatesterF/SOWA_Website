# Generated by Django 3.2.7 on 2021-09-02 09:11

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(choices=[(recipes.models.MealTypes['FIRE'], 'Campfire Cooking'), (recipes.models.MealTypes['INDOORS'], 'Indoor Catering'), (recipes.models.MealTypes['SMALL'], 'Small Group Cooking')], max_length=25),
        ),
    ]
