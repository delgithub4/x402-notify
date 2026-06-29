class ChannelManager:

    def __init__(self):

        self.channels = []

    def register(self, channel):

        self.channels.append(channel)

    def available(self):

        return self.channels
