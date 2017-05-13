from django.contrib import admin
from SlackBot.models import Team
from .models import Meal, Order

admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Team)
