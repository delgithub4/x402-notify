class TemplateService:

    def welcome(
        self,
        name
    ):

        return f"""

Welcome {name},

Thank you for joining x402.

"""

    def payment(
        self,
        amount
    ):

        return f"""

Your payment of ${amount} was successful.

"""

    def password_reset(
        self,
        link
    ):

        return f"""

Reset your password:

{link}

"""
