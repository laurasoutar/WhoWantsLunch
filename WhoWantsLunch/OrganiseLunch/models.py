from django.db import models
from django.utils import timezone



class Meal(models.Model):
    slack_channel = models.CharField(max_length=200)
    organiser_name = models.CharField(max_length=100)
    meal_name = models.CharField(max_length=100)
    meal_datetime = models.DateTimeField(default=timezone.now)
    meal_location = models.CharField(max_length=200)
    menu_URL = models.CharField(max_length=200)
    notes = models.TextField()
    
    def __str__(self):
        return self.meal_name

class Order(models.Model):
    meal = models.ForeignKey(Meal)
    name = models.CharField(max_length=100)
    starter = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.name

