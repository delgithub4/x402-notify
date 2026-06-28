class EmailProvider:

    def send(
        self,
        recipient,
        subject,
        message
    ):

        return {

            "provider": "Email",

            "recipient": recipient,

            "subject": subject,

            "status": "sent"

        }
