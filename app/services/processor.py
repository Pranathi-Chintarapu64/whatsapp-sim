from datetime import datetime
from typing import Optional

from app.models.schemas import WebhookPayload
from app.services.responses import save_response
from app.services.llm import generate_llm_response
from app.services.media import handle_media
from app.services.context import load_user_context


def process_message(payload: WebhookPayload) -> None:
    user_context = load_user_context(payload.sender)

    extracted_text: Optional[str] = None
    if payload.media:
        extracted_text = handle_media(payload.media)

    prompt = f"""
    You are a health assistant.

    User context:
    {user_context}

    User message:
    {payload.text}

    Extracted report text:
    {extracted_text}

    Provide advice related to diet, exercise, and sleep.
    """

    llm_response = generate_llm_response(prompt)

    save_response(
        message_id=payload.message_id,
        response={
            "reply": llm_response,
            "processed_at": datetime.utcnow().isoformat()
        }
    )
