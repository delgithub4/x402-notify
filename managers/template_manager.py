from providers.provider_factory import ProviderFactory


class TemplateManager:

    def __init__(self):

        self.provider = ProviderFactory.template()

    def render(
        self,
        template,
        data,
    ):

        return self.provider.render(
            template,
            data,
        )
