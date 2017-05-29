from django.conf import settings
from OrganiseLunch.models import Meal, Order
from SlackBot.adapters.chat import Chat
from SlackBot.adapters.messages.lunch_response import lunch_response
from SlackBot.models import Team

def lunch_request(data):
    token = Team.objects.get(team_id=data['team']['id']).team_access_token
    chat = Chat.from_token(token)
    result = data['actions'][0]['name']
    meal_id = data['actions'][0]['value']
    original = data['original_message']['attachments'][0]
    user = data['user']['name']
    message = ""
    if result == "lunch_yes":
        url = "{scheme}://{host}/lunches/{meal_id}/order/".format(scheme=settings.SCHEME,
                                                                  host=settings.HOST,
                                                                  meal_id=meal_id)
        message = ":white_check_mark: Accepted: Please complete your order at: {}".format(url)
    else:
        meal = Meal.objects.get(pk=meal_id)
        order = Order(attending=False, meal=meal, name=user)
        order.save()
        message = ":negative_squared_cross_mark: Declined"
    response = lunch_response(author=original['author_name'],
                              meal_name=original['title'],
                              meal_url=original['title_link'],
                              message=message,
                              date_time=original['footer'])
    chat.update_message(time_stamp=data['original_message']['ts'],
                        user_id=data['user']['id'],
                        text="",
                        attachments=[response])
