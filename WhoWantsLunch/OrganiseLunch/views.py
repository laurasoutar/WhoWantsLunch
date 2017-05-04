from django.shortcuts import render, redirect
from .models import Meal
from .models import Order

from .forms import MealForm
from .forms import OrderForm

def Lunches(request):
   meal = Meal.objects.first()
   orders = Order.objects.filter(meal=meal).all()
   return render(request, "./OrganiseLunch/meal_details.html", {'meal' : meal, 'orders' : orders})
   
def meal_view(request):
	if request.method == "POST":
		form = MealForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('menu_detail')
	else:
		form = MealForm()
	return render(request, "./OrganiseLunch/meal_setup.html", {'form' : form})