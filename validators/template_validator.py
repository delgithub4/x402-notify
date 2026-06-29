class TemplateValidator:

    @staticmethod
    def validate(template):

        if not template:

            raise ValueError(
                "Template is required."
            )

        return True
