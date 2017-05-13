import json
import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import Team

def oauth(request):
    url = 'https://slack.com/api/oauth.access'
    if 'error' in request.GET:
        return HttpResponse(request.GET['error'].replace('_', ' '))
    elif not 'code' in request.GET:
        return HttpResponse('An access code was not returned from Slack.')
    code = request.GET['code']
    params = {'code': code,
              'client_id': settings.SLACK_CLIENT_ID,
              'client_secret': settings.SLACK_CLIENT_SECRET}
    json_response = requests.get(url, params)
    data = json.loads(json_response.text)
    if not 'ok' in data or data['ok'] != True:
        return HttpResponse('The Slack bot was not created successfully.')
    if (not 'team_name' in data or not 'team_id' in data or not 'bot' in data
            or not 'bot_user_id' in data['bot'] or not 'bot_access_token' in data['bot']):
        return HttpResponse('The details about the created Slack bot are incomplete.')
    Team.objects.create(name=data['team_name'],
                        team_id=data['team_id'],
                        team_access_token=data['access_token'],
                        bot_id=data['bot']['bot_user_id'],
                        bot_access_token=data['bot']['bot_access_token'])
    return HttpResponse('The bot has been added to your Slack team!')
