from slackclient import SlackClient
from django.core.management.base import BaseCommand
from SlackBot.apps import SlackbotConfig

class Command(BaseCommand):
    help = 'Sends a message to all users about a new lunch plan'
    def handle(self, *args, **options):
        client = SlackClient(SlackbotConfig.team_key)
        user_list = client.api_call( "users.list" )['members']
        channel_list = client.api_call( "channels.list" )['channels']
        im_list = client.api_call( "im.list" )['ims']

        for user in user_list:
            if user['name'] == "scottc" or user['name'] == "simon" or "lalsoutar":
                for im in im_list:
                    if im['user'] == user['id']:
                        client.api_call(
                            "chat.postMessage",
                            channel=im['id'],
                            text="Would you like to join the team lunch at <THE PLACE> on <THE DATE> at <THE TIME>?"
                        )
