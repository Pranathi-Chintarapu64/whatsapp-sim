from datetime import datetime, timedelta
from threading import Lock

_user_last_message_time = {}
_lock = Lock()
RATE_LIMIT_WINDOW = timedelta(seconds=5)

def check_rate_limit(sender: str) -> bool:
    now = datetime.utcnow()

    with _lock:
        last_seen = _user_last_message_time.get(sender)
        if last_seen and (now - last_seen) < RATE_LIMIT_WINDOW:
            return False
        _user_last_message_time[sender] = now
        return True
