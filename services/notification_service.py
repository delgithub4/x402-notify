class NotificationService:

    def send(
        self,
        provider,
        recipient,
        subject,
        message
    ):

        return {

            "provider": provider,

            "recipient": recipient,

            "subject": subject,

            "message": message,

            "status": "queued"

        }
