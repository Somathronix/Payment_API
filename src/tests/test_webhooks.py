import hmac
import hashlib
import json


def sign(body: bytes, secret: str) -> str:
    return hmac.new(
        secret.encode(),
        body,
        hashlib.sha256
    ).hexdigest()


def test_webhook_valid(client):
    event = {
        "id": "evt_1",
        "type": "payment.updated",
        "created_at": "2026-01-01T00:00:00Z",
        "data": {
            "object": {
                "id": "pay_1",
                "type": "payin",
                "status": "succeeded"
            }
        }
    }

    raw = json.dumps(event).encode()
    signature = sign(raw, "test_webhook")

    r = client.post(
        "/v1/webhooks/events",
        data=raw,
        headers={
            "X-Signature": signature,
            "X-Event-Id": "evt_1",
            "Content-Type": "application/json"
        }
    )

    assert r.status_code == 200


def test_webhook_bad_signature(client):
    r = client.post(
        "/v1/webhooks/events",
        data=b"{}",
        headers={
            "X-Signature": "bad",
            "X-Event-Id": "evt_1",
            "Content-Type": "application/json"
        }
    )

    assert r.status_code == 401
