class PushProvider:

    async def send(
        self,
        device,
        title,
        body,
    ):

        return {
            "channel": "push",
            "device": device,
            "status": "queued",
        }
