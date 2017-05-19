from slackclient import SlackClient

class Adapter(object):

    def __init__(self, client):
        self.client = client

    @classmethod
    def from_adapter(cls, adapter):
        return cls(adapter.client)

    @classmethod
    def from_token(cls, team_access_token):
        return cls(SlackClient(team_access_token))

    def api_call(self, method, **kwargs):
        result = self.client.api_call(method, **kwargs)
        if result['ok'] is True:
            return result
        raise ValueError(result)
