class SMSProvider:

    def send(
        self,
        recipient,
        message
    ):

        return {

            "provider": "SMS",

            "recipient": recipient,

            "status": "sent"

        }
