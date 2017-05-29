import json
import threading
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .adapters.callbacks.lunch_request import lunch_request

@csrf_exempt
def process(request):
    post = request.POST
    payload = post.get('payload')
    data = json.loads(payload)
    if data['token'] == settings.SLACK_VERIFICATION_TOKEN:
        callback_id = data['callback_id']
        if callback_id in ALLOWED_METHODS:
            thread = threading.Thread(target=ALLOWED_METHODS[callback_id], args=[data], daemon=True)
            thread.start()
            return HttpResponse()

ALLOWED_METHODS = {
    'lunch_request': lunch_request
}
