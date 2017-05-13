import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process(request):
    post = request.POST
    payload = post.get('payload')
    j = json.loads(payload)
    result = j['actions'][0]['name']
    order_url = j['actions'][0]['value']
    # channel = j['channel']['id']
    if result == "lunch_yes":
        return HttpResponse("Excellent, see you there!! Please select your food at: {}"
                            .format(order_url))
    else:
        return HttpResponse("Of all the humans, you are amongst the worst!")
