from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig
import time
class Command(BaseCommand):
    help = 'Listens for events on our slack teams client'

    def __init__(self):
        self.client = SlackClient(SlackbotConfig.team_key)

    def handle(self, *args, **options):
        if self.client.rtm_connect():
            while True:
                events = self.client.rtm_read()
                for event in events:
                    try:
                        if event['type']=='message':
                            if event['text'].lower()=='yes':
                                self.client.rtm_send_message(
                                    event['channel'],
                                    "Excellent, see you there!!!"
                                )
                            if event['text'].lower()=='no':
                                self.client.rtm_send_message(
                                    event['channel'],
                                    "Of all the humans, you are amongst the worst!"
                                )
                    except:
                        print (event)
                        print ("failed")


                time.sleep(1)

    def affirmative(self, channel):
        pass

    def denied(self, channel):
        pass