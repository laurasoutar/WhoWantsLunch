import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process(request):
    post = request.POST
    payload = post.get('payload')
    j = json.loads(payload)
    if j['token'] == settings.SLACK_VERIFICATION_TOKEN:
        callback_id = j['callback_id']
        actions = j['actions']
        if callback_id in ALLOWED_METHODS:
            return ALLOWED_METHODS[callback_id](actions)

def lunch_request(actions):
    action = actions[0]
    result = action['name']
    order_url = action['value']
    if result == "lunch_yes":
        return HttpResponse("Excellent, see you there!! Please select your food at: {}"
                            .format(order_url))
    else:
        return HttpResponse("Of all the humans, you are amongst the worst!")

ALLOWED_METHODS = {
    'lunch_request': lunch_request
}
