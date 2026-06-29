from providers.provider_factory import ProviderFactory


class NotificationManager:

    def __init__(self):

        self.email = ProviderFactory.email()

        self.sms = ProviderFactory.sms()

        self.push = ProviderFactory.push()

        self.webhook = ProviderFactory.webhook()
