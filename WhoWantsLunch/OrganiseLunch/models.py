from django.db import models
from django.utils import timezone

class Meal(models.Model):
	organiser_name = models.CharField(max_length=100)
	## To add ForeignKey('auth.User')
	meal_name = models.CharField(max_length=100, null=False, blank=False)
	meal_datetime = models.DateTimeField(default=timezone.now, null=False, blank=False)
	meal_location = models.CharField(max_length=200, null=False, blank=False)
	menu_URL = models.CharField(max_length=200, null=False, blank=False)
	slack_channel = models.CharField(max_length=200, null=False, blank=False)
	notes = models.TextField()
	
    def __str__(self):
    return self.meal_name

class Order(models.Model):
    meal = models.ForeignKey(Meal)
    name = models.CharField(max_length=100, null=False, blank=False)
    starter = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    drink = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.name

