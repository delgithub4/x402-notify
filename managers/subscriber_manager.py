class SubscriberManager:

    def __init__(self):

        self.subscribers = []

    def subscribe(self, subscriber):

        self.subscribers.append(subscriber)

    def all(self):

        return self.subscribers
