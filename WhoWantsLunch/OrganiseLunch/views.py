from django.core.management import call_command
from django.shortcuts import render, redirect
from .models import Meal, Order
from .forms import OrderForm, MealForm

# Create your views here.
def lunches(request):
    meal = Meal.objects.first()
    orders = Order.objects.filter(meal=meal).all()
    return render(request, "meal_details.html", {'meal': meal, 'orders': orders})

def home(request):
    return render(request, "home.html", {})

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

    return render(request, "order_response.html", {'form': form, 'meal': meal})

def meal_view(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            new_meal = form.save()
            call_command("lunch_send",
                         place=new_meal.meal_location,
                         datetime=new_meal.meal_datetime,
                         id=new_meal.pk)
            return redirect('home')
    else:
        form = MealForm()

    return render(request, "meal_setup.html", {'form' : form})
