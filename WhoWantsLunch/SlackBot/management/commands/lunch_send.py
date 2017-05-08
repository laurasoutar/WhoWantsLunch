import time
from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig

class Command(BaseCommand):
    help = 'Sends a message to all users about a new lunch plan'

    def add_arguments(self, parser):
        parser.add_argument('--place', dest='place', default='Nandos')
        parser.add_argument('--date', dest='date', default=time.strftime("%d/%m/%Y"))
        parser.add_argument('--time', dest='time', default='13:00')
        parser.add_argument('--id', dest='lunch_id', default='0')

    def handle(self, *args, **options):
        question = "Would you like to join the team lunch at {} on {} at {}?".format(
            options['place'], options['date'], options['time'])
        client = SlackClient(SlackbotConfig.team_key)
        user_list = client.api_call("users.list")['members']
        # channel_list = client.api_call("channels.list")['channels']
        im_list = client.api_call("im.list")['ims']

        for user in user_list:
            if not user['is_bot'] and not user['name'] == 'slackbot':
                for im_channel in im_list:
                    if im_channel['user'] == user['id']:
                        client.api_call(
                            "chat.postMessage",
                            channel=im_channel['id'],
                            text="",
                            attachments=[
                                {
                                    "text": question,
                                    "fallback": "Youse’uns Want Lunch?",
                                    "callback_id": "lunch_response",
                                    "color": "#c55100",
                                    "attachment_type": "default",
                                    "actions": [
                                        {
                                            "name": "lunch_yes",
                                            "text": "Yes",
                                            "type": "button",
                                            "value": options['lunch_id']
                                        },
                                        {
                                            "name": "lunch_no",
                                            "text": "No",
                                            "type": "button",
                                            "value": options['lunch_id']
                                        }
                                    ]
                                }
                            ]
                        )
