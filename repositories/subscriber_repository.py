class SubscriberRepository:

    def __init__(self):

        self.subscribers = []

    def save(self, subscriber):

        self.subscribers.append(subscriber)

    def all(self):

        return self.subscribers
