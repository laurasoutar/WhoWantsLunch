from .adapter import Adapter
from .channel import Channel
from .im import Im

class Chat(Adapter):

    def post_message(self, channel, text, attachments=None):
        return self.api_call("chat.postMessage", channel=channel, text=text,
                             attachments=attachments)

    def post_message_to_members(self, channel, text, attachments=None):
        channel_adapter = Channel.from_adapter(self)
        im_adapter = Im.from_adapter(self)
        member_ids = channel_adapter.member_ids(channel)
        im_list = im_adapter.list()
        for member_id in member_ids:
            for im_channel in im_list:
                if im_channel['user'] == member_id:
                    return self.post_message(channel=im_channel['id'], text=text,
                                             attachments=attachments)
