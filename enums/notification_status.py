from enum import Enum


class NotificationStatus(str, Enum):

    QUEUED = "queued"

    PROCESSING = "processing"

    SENT = "sent"

    FAILED = "failed"

    DELIVERED = "delivered"
