import json
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from SlackBot.adapters.channel import Channel
from SlackBot.adapters.chat import Chat
from SlackBot.adapters.messages.lunch_request import lunch_request
from SlackBot.models import Team
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
        form = OrderForm(initial={'attending': 'true', 'meal': meal})

    return render(request, "order_response.html", {'form': form, 'meal': meal})

def meal_view(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            new_meal = form.save()
            author = "{name} / #{channel}".format(name=new_meal.organiser_name,
                                                  channel=new_meal.slack_channel)
            meal_name = "{name} at {location}".format(name=new_meal.meal_name,
                                                      location=new_meal.meal_location)
            message = "Would you like to attend this team lunch?"
            date_time = new_meal.meal_datetime.strftime('%A %d %B %Y at %H:%M')
            message = lunch_request(notification=meal_name,
                                    author=author,
                                    meal_id=new_meal.pk,
                                    meal_name=meal_name,
                                    meal_url=new_meal.menu_URL,
                                    message=message,
                                    date_time=date_time)
            chat = Chat.from_token(new_meal.team.team_access_token)
            chat.post_message_to_members(new_meal.slack_channel, "", attachments=[message])
            return redirect('home')
    else:
        form = MealForm()

    return render(request, "meal_setup.html", {'form' : form})

@csrf_exempt
def get_slack_channels(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        team_id = data['team_id']
        team = Team.objects.get(pk=team_id)
        channel = Channel.from_token(team.team_access_token)
        slack_channels = channel.list_names()
        return HttpResponse(json.dumps(slack_channels), content_type="application/json")
