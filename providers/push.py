class PushProvider:

    def send(
        self,
        recipient,
        message
    ):

        return {

            "provider": "Push",

            "recipient": recipient,

            "status": "sent"

        }
