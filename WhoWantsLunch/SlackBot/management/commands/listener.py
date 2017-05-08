import time
from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig

class Command(BaseCommand):
    help = 'Listens for events on our slack teams client'

    def __init__(self):
        super(Command, self).__init__()
        self.client = SlackClient(SlackbotConfig.team_key)

    def handle(self, *args, **options):
        if self.client.rtm_connect():
            while True:
                events = self.client.rtm_read()
                for event in events:
                    try:
                        if event['type'] == 'message':
                            if event['text'].lower() == 'yes':
                                self.affirmative(event['channel'])
                            if event['text'].lower() == 'no':
                                self.denied(event['channel'])
                    except:
                        pass

                time.sleep(1)

    def affirmative(self, channel):
        self.client.rtm_send_message(channel, "Excellent, see you there!!!")

    def denied(self, channel):
        self.client.rtm_send_message(channel, "Of all the humans, you are amongst the worst!")
