import json
import os

USER_CONTEXT_FILE = "data/user_context.json"


def load_user_context(user_id: str) -> dict:
    if not os.path.exists(USER_CONTEXT_FILE):
        return {}

    if os.path.getsize(USER_CONTEXT_FILE) == 0:
        return {}

    try:
        with open(USER_CONTEXT_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return {}

    return data.get(user_id, {})
