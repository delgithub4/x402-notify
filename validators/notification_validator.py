class NotificationValidator:

    @staticmethod
    def validate(notification):

        if notification is None:

            raise ValueError(
                "Notification is required."
            )

        return True
