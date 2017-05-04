from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig

class Command(BaseCommand):
    help = 'Sends a message to all users about a new lunch plan'
    def handle(self, *args, **options):
        client = SlackClient(SlackbotConfig.team_key)
        user_list = client.api_call( "users.list" )
        channel_list = client.api_call( "channels.list" )
        
        print (user_list['members'][0])
        print (channel_list['channels'][0])