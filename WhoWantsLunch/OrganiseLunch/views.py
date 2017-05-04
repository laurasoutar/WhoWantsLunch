from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Meal

# Create your views here.
def Lunches(request):
	meals = Meal.objects.all()
	return render(request, "./OrganiseLunch/meal_details.html", {'meals' : meals})