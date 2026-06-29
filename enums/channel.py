from enum import Enum


class Channel(str, Enum):

    EMAIL = "email"

    SMS = "sms"

    PUSH = "push"

    WEBHOOK = "webhook"
