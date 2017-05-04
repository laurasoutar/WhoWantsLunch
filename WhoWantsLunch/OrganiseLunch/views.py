from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Meal
from .models import Order

# Create your views here.
def Lunches(request):
	meal = Meal.objects.first()
	orders = Order.objects.filter(meal=meal).all()
	return render(request, "./OrganiseLunch/meal_details.html", {'meal' : meal, 'orders' : orders})

def Home(request):
	return render(request, "./OrganiseLunch/home.html", {})