from fastapi import APIRouter, HTTPException, status

from app.services.responses import get_response

router = APIRouter(prefix="/responses", tags=["Responses"])


@router.get("/{message_id}", status_code=status.HTTP_200_OK)
def fetch_response(message_id: str):
    response = get_response(message_id)

    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Response not ready or message_id not found",
        )

    return response
