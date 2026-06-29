class WebhookProvider:

    async def send(
        self,
        url,
        payload,
    ):

        return {
            "channel": "webhook",
            "url": url,
            "status": "queued",
        }
