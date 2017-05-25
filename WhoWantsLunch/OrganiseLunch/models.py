from django.db import models
from django.utils import timezone
from SlackBot.models import Team

class Meal(models.Model):
    organiser_name = models.CharField(max_length=100)
    ## To add ForeignKey('auth.User')
    meal_name = models.CharField(max_length=100, null=False, blank=False)
    meal_datetime = models.DateTimeField(default=timezone.now, null=False, blank=False)
    meal_location = models.CharField(max_length=200, null=False, blank=False)
    menu_URL = models.CharField(max_length=200, null=False, blank=False)
    slack_channel = models.CharField(max_length=200, null=False, blank=False)
    notes = models.TextField(max_length=200, null=True, blank=True)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.meal_name

class Order(models.Model):
    meal = models.ForeignKey(Meal)
    name = models.CharField(max_length=100, null=False, blank=False)
    attending = models.BooleanField()
    starter = models.CharField(max_length=100, null=True, blank=True)
    main = models.CharField(max_length=100, null=True, blank=True)
    dessert = models.CharField(max_length=100, null=True, blank=True)
    drink = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
