from .adapter import Adapter

class User(Adapter):

    def info(self, user_id):
        return self.api_call("users.info", user=user_id)["user"]

    def name(self, user_id):
        return self.api_call("users.info", user=user_id)["user"]["name"]
