from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from .models import Meal
from .forms import OrderForm

# Create your views here.
def Lunches(request):
	meal = Meal.objects.first()
	orders = Order.objects.filter(meal=meal).all()
	return render(request, "./OrganiseLunch/meal_details.html", {'meal' : meal, 'orders' : orders})

def Home(request):
	return render(request, "./OrganiseLunch/home.html", {})

def Order(request, meal_id):
	meal = Meal.objects.get(pk=meal_id)
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('all-borrowed') )
	else:
		form = OrderForm(initial={})
		form.meal = meal

	return render(request, "./OrganiseLunch/order_response.html", {'form': form, 'meal': meal})