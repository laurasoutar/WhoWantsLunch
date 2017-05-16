from slackclient import SlackClient

class Adapter(object):

    def __init__(self, team_access_token):
        self.client = SlackClient(team_access_token)
