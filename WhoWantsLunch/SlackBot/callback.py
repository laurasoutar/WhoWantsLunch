import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from OrganiseLunch.models import Meal, Order

@csrf_exempt
def process(request):
    post = request.POST
    payload = post.get('payload')
    data = json.loads(payload)
    if data['token'] == settings.SLACK_VERIFICATION_TOKEN:
        callback_id = data['callback_id']
        if callback_id in ALLOWED_METHODS:
            return ALLOWED_METHODS[callback_id](data)

def lunch_request(data):
    result = data['actions'][0]['name']
    meal_id = data['actions'][0]['value']
    user = data['user']['name']
    if result == "lunch_yes":
        url = "{scheme}://{host}/lunches/{meal_id}/order/".format(scheme=settings.SCHEME,
                                                                  host=settings.HOST,
                                                                  meal_id=meal_id)
        message = "Great! :grinning: Please complete your order at: {}".format(url)
        return HttpResponse(message)
    else:
        meal = Meal.objects.get(pk=meal_id)
        order = Order(attending=False, meal=meal, name=user)
        order.save()
        return HttpResponse("No problem. Maybe another time. :simple_smile:")

ALLOWED_METHODS = {
    'lunch_request': lunch_request
}
