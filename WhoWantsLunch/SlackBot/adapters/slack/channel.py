from .adapter import Adapter

class Channel(Adapter):

    def members(self, channel):
        channels_list = self.client.api_call("channels.list")
        if 'channels' in channels_list:
            for channel_info in channels_list['channels']:
                if ('name' in channel_info) and (channel_info['name'] == channel):
                    return channel_info['members']
