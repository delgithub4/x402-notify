from providers.email import EmailProvider
from providers.sms import SMSProvider
from providers.push import PushProvider

class NotificationService:

    def __init__(self):

        self.email = EmailProvider()

        self.sms = SMSProvider()

        self.push = PushProvider()

    def send(
        self,
        provider,
        recipient,
        subject="",
        message=""
    ):

    if provider == "email":

        return self.email.send(
            recipient,
            subject,
            message
        )

    if provider == "sms":

        return self.sms.send(
            recipient,
            message
        )

    if provider == "push":

        return self.push.send(
            recipient,
            message
        )

    return {

        "status": "unsupported provider"

    }   

        return {

            "provider": provider,

            "recipient": recipient,

            "subject": subject,

            "message": message,

            "status": "queued"

        }
