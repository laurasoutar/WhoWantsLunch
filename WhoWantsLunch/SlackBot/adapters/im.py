from .adapter import Adapter

class Im(Adapter):

    def list(self):
        return self.api_call("im.list")["ims"]
