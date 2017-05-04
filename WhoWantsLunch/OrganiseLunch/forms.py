from django import forms
from .models import Meal
from .models import Order

class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
		fields = ('organiser_name', 'meal_name', 'meal_datetime', 'meal_location', 'menu_URL', 'slack_channel', 'notes',)

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('meal', 'name', 'starter', 'main', 'dessert', 'drink', 'notes')
		widgets = {'meal': forms.HiddenInput()}

