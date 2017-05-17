from .adapter import Adapter
from .user import User

class Channel(Adapter):

    def member_ids(self, channel_name):
        channels_list = self.api_call("channels.list")
        for channel_info in channels_list['channels']:
            if channel_info['name'] == channel_name:
                return channel_info['members']

    def member_names(self, channel_name):
        member_ids = self.member_ids(channel_name)
        member_names = []
        user_adapter = User.from_adapter(self)
        for user_id in member_ids:
            member_names.append(user_adapter.name(user_id))
        member_names.sort()
        return member_names
