from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_rate_limit_same_user():
    payload_1 = {
        "message_id": "msg-101",
        "from": "user_rate",
        "text": "hello",
        "timestamp": "2025-01-01T10:00:00",
        "media": None
    }

    payload_2 = {
        "message_id": "msg-102",
        "from": "user_rate",
        "text": "another message",
        "timestamp": "2025-01-01T10:00:01",
        "media": None
    }

    res1 = client.post("/webhook", json=payload_1)
    assert res1.status_code == 200

    res2 = client.post("/webhook", json=payload_2)
    assert res2.status_code == 429
