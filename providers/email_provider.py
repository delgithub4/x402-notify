class EmailProvider:

    async def send(
        self,
        recipient,
        subject,
        body,
    ):

        return {
            "channel": "email",
            "recipient": recipient,
            "status": "queued",
        }
