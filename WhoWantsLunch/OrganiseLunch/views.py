from django.conf import settings
from django.shortcuts import render, redirect
from SlackBot.adapters.chat import Chat
from SlackBot.adapters.messages.lunch_request import lunch_request
from .models import Meal, Order
from .forms import OrderForm, MealForm

# Create your views here.
def lunches(request):
    meal = Meal.objects.first()
    orders = Order.objects.filter(meal=meal).all()
    return render(request, "meal_details.html", {'meal': meal, 'orders': orders})

def home(request):
    return render(request, "home.html")

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
            question = "Would you like to join the team lunch at {} on {}?".format(
                new_meal.meal_location, new_meal.meal_datetime)
            url = '{scheme}://{host}/lunches/{lunch_id}/order/'.format(scheme=settings.SCHEME,
                                                                       host=settings.HOST,
                                                                       lunch_id=new_meal.pk)
            message = lunch_request(question, url)
            chat = Chat.from_token(new_meal.team.team_access_token)
            chat.post_message_to_members(new_meal.slack_channel, "", attachments=[message])
            return redirect('home')
    else:
        form = MealForm()

    return render(request, "meal_setup.html", {'form' : form})
