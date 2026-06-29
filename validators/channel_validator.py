class ChannelValidator:

    @staticmethod
    def validate(channel):

        if not channel:

            raise ValueError(
                "Channel is required."
            )

        return True
