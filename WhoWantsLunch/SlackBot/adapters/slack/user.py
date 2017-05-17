from .adapter import Adapter

class User(Adapter):

    def name(self, user_id):
        return self.api_call("users.info", user=user_id)["user"]["name"]
