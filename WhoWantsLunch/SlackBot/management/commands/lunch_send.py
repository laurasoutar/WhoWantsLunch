from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig
import time

class Command(BaseCommand):
    help = 'Sends a message to all users about a new lunch plan'

    def add_arguments(self, parser):
        parser.add_argument(
            '--place', 
            dest='place',
            default='Nandos',
        )
        parser.add_argument(
            '--date', 
            dest='date',
            default=time.strftime("%d/%m/%Y"),
        )
        parser.add_argument(
            '--time', 
            dest='time',
            default='13:00',
        )


    def handle(self, *args, **options):
        client = SlackClient(SlackbotConfig.team_key)
        user_list = client.api_call( "users.list" )['members']
        channel_list = client.api_call( "channels.list" )['channels']
        im_list = client.api_call( "im.list" )['ims']

        for user in user_list:
            if not user['is_bot'] and not user['name'] == 'slackbot':
                for im in im_list:
                    if im['user'] == user['id']:


                        question = "Would you like to join the team lunch at "+ options['place'] +" on "+ options['date'] +" at "+ options['time'] +"?"
                        client.api_call(
                            "chat.postMessage",
                            channel=im['id'],
                            text="",
                            #text="Would you like to join the team lunch at "+ options['place'] +" on "+ options['date'] +" at "+ options['time'] +"?" 
                            attachments=[
                                {
                                    "text": question,
                                    "fallback": "Youse’uns Want Lunch?",
                                    "callback_id": "lunch_response",
                                    "color": "#c55100",
                                    "attachment_type": "default",
                                    "actions": [
                                        {
                                            "name": "lunch_response",
                                            "text": "Yes",
                                            "type": "button",
                                            "value": "yes"
                                        },
                                        {
                                            "name": "lunch_response",
                                            "text": "No",
                                            "type": "button",
                                            "value": "no"
                                        }
                                    ]
                                }
                            ]
                        )
