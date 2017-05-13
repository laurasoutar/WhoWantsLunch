from django.conf import settings

def slack_processor(request):
    return {'slack_client_id': settings.SLACK_CLIENT_ID}
