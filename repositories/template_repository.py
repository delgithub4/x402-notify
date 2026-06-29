class TemplateRepository:

    def __init__(self):

        self.templates = {}

    def save(
        self,
        name,
        template,
    ):

        self.templates[name] = template

    def get(self, name):

        return self.templates.get(name)
