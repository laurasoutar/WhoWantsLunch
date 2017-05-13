import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

URL = '{scheme}://{host}/lunches/{lunch_id}/order/'.format(scheme=settings.SCHEME,
                                                           host=settings.HOST,
                                                           lunch_id='{}')

@csrf_exempt
def process(request):
    post = request.POST
    payload = post.get('payload')
    j = json.loads(payload)
    result = j['actions'][0]['name']
    result_id = j['actions'][0]['value']
    # channel = j['channel']['id']
    if result == "lunch_yes":
        return HttpResponse("Excellent, see you there!! Please select your food at: {}"
                            .format(URL.format(result_id)))
    else:
        return HttpResponse("Of all the humans, you are amongst the worst!")
