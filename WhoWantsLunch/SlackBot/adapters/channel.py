from .adapter import Adapter
from .user import User

class Channel(Adapter):

    def member_ids(self, channel):
        channels_list = self.api_call("channels.list")
        for channel_info in channels_list['channels']:
            if channel_info['name'] == channel:
                return channel_info['members']

    def member_infos(self, channel):
        member_ids = self.member_ids(channel)
        member_infos = []
        user_adapter = User.from_adapter(self)
        for user_id in member_ids:
            member_infos.append(user_adapter.info(user_id))
        return member_infos

    def member_names(self, channel):
        member_ids = self.member_ids(channel)
        member_names = []
        user_adapter = User.from_adapter(self)
        for user_id in member_ids:
            member_names.append(user_adapter.name(user_id))
        member_names.sort()
        return member_names
