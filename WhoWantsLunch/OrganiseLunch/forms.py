from django import forms
from .models import meal
from .models import order

class LunchForm(forms.ModelForm):
	class Meta:
		model = lunch
		fields = ('', 'lunchName', 'lunchTime', 'lunchLocation', 'menuLink', 'lunchNotes',)

class OrderForm(forms.ModelForm):
	class Meta:
		model = order
		fields = ('starter', 'main', 'dessert', 'drink', 'orderNotes',)