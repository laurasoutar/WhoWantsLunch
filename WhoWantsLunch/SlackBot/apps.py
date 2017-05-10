from django.apps import AppConfig

class SlackbotConfig(AppConfig):
    name = 'SlackBot'
    # TO DO: Make configurable with the Add to Slack button
    team_key = ''
