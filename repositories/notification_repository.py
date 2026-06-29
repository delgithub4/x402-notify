class NotificationRepository:

    def __init__(self):

        self.notifications = []

    def save(self, notification):

        self.notifications.append(notification)

    def all(self):

        return self.notifications
