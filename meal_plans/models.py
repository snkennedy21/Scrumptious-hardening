from codecs import namereplace_errors
from tkinter import N
from django.db import models
from django.conf import settings
from recipes.models import USER_MODEL

USER_MODEL = settings.AUTH_USER_MODEL

class MealPlan(models.Model):
  name = models.CharField(max_length=120)
  owner = models.ForeignKey(USER_MODEL, related_name="meal_plans", on_delete=models.CASCADE)
  date = models.DateField()
  recipes = models.ManyToManyField('recipes.Recipe', related_name="meal_plans")
