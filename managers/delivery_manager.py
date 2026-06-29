class DeliveryManager:

    def __init__(self):

        self.queue = []

    def enqueue(self, notification):

        self.queue.append(notification)

    def pending(self):

        return self.queue
