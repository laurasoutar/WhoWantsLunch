from django import forms
from .models import Meal, Order

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('team', 'organiser_name', 'meal_name', 'meal_datetime', 'meal_location',
                  'menu_URL', 'slack_channel', 'notes')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('meal', 'name', 'attending', 'starter', 'main', 'dessert', 'drink', 'notes')

