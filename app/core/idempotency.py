import hashlib
from threading import Lock
_processed_messages = set()
_lock = Lock()

def _generate_key(message_id: str, timestamp: str) -> str:
    raw_key = f"{message_id}:{timestamp}"
    return hashlib.sha256(raw_key.encode()).hexdigest()

def is_duplicate(message_id: str, timestamp: str) -> bool:
    key = _generate_key(message_id, timestamp)

    with _lock:
        return key in _processed_messages

def mark_processed(message_id: str, timestamp: str) -> None:
    key = _generate_key(message_id, timestamp)

    with _lock:
        _processed_messages.add(key)