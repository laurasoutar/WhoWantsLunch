from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def process( request ):
	post = request.POST
	payload = post.get('payload')

	j = json.loads(payload)
	result = j['actions'][0]['value']
	channel = j['channel']['id']

	if result == "yes":
		return HttpResponse("Excellent, see you there!!")

	return HttpResponse("Of all the humans, you are amongst the worst!")