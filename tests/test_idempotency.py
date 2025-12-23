from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_duplicate_message_idempotency():
    payload = {
        "message_id": "msg-001",
        "from": "user123",
        "text": "low blood sugar",
        "timestamp": "2025-01-01T10:00:00",
        "media": None
    }

    res1 = client.post("/webhook", json=payload)
    assert res1.status_code == 200

    res2 = client.post("/webhook", json=payload)
    assert res2.status_code == 200

    response = client.get("/responses/msg-001")
    assert response.status_code == 200
