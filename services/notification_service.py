from providers.email import EmailProvider
from providers.sms import SMSProvider
from providers.push import PushProvider
from services.template_service import TemplateService

class NotificationService:

    def __init__(self):

        self.email = EmailProvider()

        self.sms = SMSProvider()

        self.push = PushProvider()

        self.template = TemplateService()

    def send(
        self,
        provider,
        recipient,
        subject="",
        message=""
    ):

    def send_welcome(
        self,
        recipient,
        name
    ):

        message = self.template.welcome(name)
    
        return self.email.send(
    
            recipient,
    
            "Welcome!",
    
            message
    
        )
    
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
