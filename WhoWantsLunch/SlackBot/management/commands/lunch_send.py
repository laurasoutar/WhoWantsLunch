from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig

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
            default='1970-01-01',
        )
        parser.add_argument(
            '--time', 
            dest='time',
            default='13:00',
        )


    def handle(self, *args, **options):
        print (options)

        client = SlackClient(SlackbotConfig.team_key)
        user_list = client.api_call( "users.list" )['members']
        channel_list = client.api_call( "channels.list" )['channels']
        im_list = client.api_call( "im.list" )['ims']

        for user in user_list:
            if user['name'] == "scottc" or "simon":
                for im in im_list:
                    if im['user'] == user['id']:
                        client.api_call(
                            "chat.postMessage",
                            channel=im['id'],
                            text="Would you like to join the team lunch at "+ options['place'] +" on "+ options['date'] +" at "+ options['time'] +"?"
                        )
