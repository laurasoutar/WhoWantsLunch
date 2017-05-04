from django import forms
from .models import lunch
from .models import order

class LunchForm(forms.ModelForm):
	class Meta:
		model = lunch
		fields = ('organiserName', 'lunchName', 'lunchTime', 'lunchLocation', 'menuLink', 'lunchNotes')