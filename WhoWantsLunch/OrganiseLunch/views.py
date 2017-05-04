from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from .models import Meal, Order
from .forms import OrderForm, MealForm

# Create your views here.
def Lunches(request):
	meal = Meal.objects.first()
	orders = Order.objects.filter(meal=meal).all()
	return render(request, "./OrganiseLunch/meal_details.html", {'meal' : meal, 'orders' : orders})

def Home(request):
	return render(request, "./OrganiseLunch/home.html", {})

def OrderView(request, meal_id):
	meal = Meal.objects.get(pk=meal_id)
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.meal = meal
			form.save()
			return redirect('home')
	else:
		form = OrderForm(initial={})
		form.meal = meal

	return render(request, "./OrganiseLunch/order_response.html", {'form': form, 'meal': meal})

def meal_view(request):
	if request.method == "POST":
		form = MealForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = MealForm()

	return render(request, "./OrganiseLunch/meal_setup.html", {'form' : form})
