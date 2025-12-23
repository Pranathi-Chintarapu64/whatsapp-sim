from app.core.store import save, get


def save_response(message_id: str, response: dict) -> None:
    save(message_id, response)


def get_response(message_id: str) -> dict | None:
    data = get(message_id)
    if not data:
        return None

    return {
        "message_id": message_id,
        **data,
    }
