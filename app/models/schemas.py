from typing import Optional
from pydantic import BaseModel, Field


class WebhookPayload(BaseModel):

    message_id: str = Field(..., description="Unique message identifier")
    sender: str = Field(..., alias="from", description="Sender user ID")
    text: str = Field(..., description="Message text sent by the user")
    timestamp: str = Field(..., description="Message timestamp")
    media: Optional[str] = Field(
        default=None,
        description="Optional media file name (e.g., report.pdf)",
    )
