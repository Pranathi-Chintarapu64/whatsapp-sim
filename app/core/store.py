from threading import Lock
from typing import Dict, Any

_responses: Dict[str, Dict[str, Any]] = {}
_lock = Lock()


def save(message_id: str, response: dict) -> None:
    with _lock:
        _responses[message_id] = response


def get(message_id: str) -> dict | None:
    with _lock:
        return _responses.get(message_id)
