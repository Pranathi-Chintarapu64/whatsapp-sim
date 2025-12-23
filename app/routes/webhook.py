from fastapi import APIRouter, BackgroundTasks, HTTPException, status

from app.models.schemas import WebhookPayload
from app.core.idempotency import is_duplicate, mark_processed
from app.core.rate_limit import check_rate_limit
from app.services.processor import process_message

router = APIRouter(prefix="/webhook", tags=["Webhook"])


@router.post("", status_code=status.HTTP_200_OK)
def receive_webhook(
    payload: WebhookPayload,
    background_tasks: BackgroundTasks,
):

    if is_duplicate(payload.message_id, payload.timestamp):
        return {
            "status": "duplicate_ignored",
            "message_id": payload.message_id
        }

    if not check_rate_limit(payload.sender):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please wait before sending next message.",
        )

    mark_processed(payload.message_id, payload.timestamp)
    background_tasks.add_task(process_message, payload)
    return {
        "status": "accepted",
        "message_id": payload.message_id
    }
