class TemplateProvider:

    def render(
        self,
        template,
        data,
    ):

        return template.format(**data)
