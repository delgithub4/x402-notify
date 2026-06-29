from providers.email_provider import EmailProvider
from providers.push_provider import PushProvider
from providers.sms_provider import SMSProvider
from providers.template_provider import TemplateProvider
from providers.webhook_provider import WebhookProvider


class ProviderFactory:

    _instances = {}

    @classmethod
    def email(cls):

        if "email" not in cls._instances:
            cls._instances["email"] = EmailProvider()

        return cls._instances["email"]

    @classmethod
    def sms(cls):

        if "sms" not in cls._instances:
            cls._instances["sms"] = SMSProvider()

        return cls._instances["sms"]

    @classmethod
    def push(cls):

        if "push" not in cls._instances:
            cls._instances["push"] = PushProvider()

        return cls._instances["push"]

    @classmethod
    def webhook(cls):

        if "webhook" not in cls._instances:
            cls._instances["webhook"] = WebhookProvider()

        return cls._instances["webhook"]

    @classmethod
    def template(cls):

        if "template" not in cls._instances:
            cls._instances["template"] = TemplateProvider()

        return cls._instances["template"]
