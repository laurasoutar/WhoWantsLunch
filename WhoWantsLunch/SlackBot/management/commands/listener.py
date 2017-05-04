### slackbot/management/commands/listener.py
from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig
import time
class Command(BaseCommand):
    help = 'Starts the bot for the first'
    def handle(self, *args, **options):
        client = SlackClient(SlackbotConfig.team_key)
        if client.rtm_connect():
            while True:
                events = client.rtm_read()
                for event in events:
                    try:
                        if event['type']=='message':
                            print (event) 
                            if event['text']=='hi':
                                client.rtm_send_message(
                                    event['channel'],
                                    "Hello World!"
                                )
                    except:
                        print ("failed")


                time.sleep(1)
