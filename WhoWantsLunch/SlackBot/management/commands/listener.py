### slackbot/management/commands/listener.py
from slackclient import SlackClient
from django.core.management.base import BaseCommand
import time
class Command(BaseCommand):
    help = 'Starts the bot for the first'
    def handle(self, *args, **options):
        client = SlackClient('xoxb-179408173191-E8sjwhEkQf43ZUUdmMTyeUYD')
        if client.rtm_connect():
            while True:
                events = client.rtm_read()
                for event in events:
                    try:
                        if event['type']=='message' and event['text']=='hi':
                            client.rtm_send_message(
                                event['channel'],
                                "Hello World!"
                            )
                    except:
                        print ("That doesn't work")


                time.sleep(1)
