from typing import Any

from pydantic import BaseModel


class NotificationRequest(BaseModel):
    recipient: str
    channel: str
    subject: str | None = None
    message: str
    metadata: dict[str, Any] = {}


class NotificationResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
