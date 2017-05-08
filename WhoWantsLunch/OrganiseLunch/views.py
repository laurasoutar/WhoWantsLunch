from django.shortcuts import render, redirect
from .models import Meal, Order
from .forms import OrderForm, MealForm

# Create your views here.
def lunches(request):
    meal = Meal.objects.first()
    orders = Order.objects.filter(meal=meal).all()
    return render(request, "./OrganiseLunch/meal_details.html", {'meal': meal, 'orders': orders})

def home(request):
    return render(request, "./OrganiseLunch/home.html", {})

def order_view(request, meal_id):
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
