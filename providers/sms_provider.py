class SMSProvider:

    async def send(
        self,
        recipient,
        message,
    ):

        return {
            "channel": "sms",
            "recipient": recipient,
            "status": "queued",
        }
