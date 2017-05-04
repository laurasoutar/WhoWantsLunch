from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig
import time
class Command(BaseCommand):
    help = 'Listens for events on our slack teams client'
    def handle(self, *args, **options):
        client = SlackClient(SlackbotConfig.team_key)
        if client.rtm_connect():
            while True:
                events = client.rtm_read()
                for event in events:
                    try:
                        if event['type']=='message':
                            if event['text'].lower()=='yes':
                                client.rtm_send_message(
                                    event['channel'],
                                    "Excellent, see you there!!!"
                                )
                            if event['text'].lower()=='no':
                                client.rtm_send_message(
                                    event['channel'],
                                    "Of all the humans, you are amongst the worst!"
                                )
                    except:
                        print (event)
                        print ("failed")


                time.sleep(1)
