def test_health_ok(client, auth_headers):
    r = client.get("/health", headers=auth_headers)

    assert r.status_code == 200
    data = r.json()

    assert data["ok"] is True
    assert "ts" in data


def test_health_unauthorized(client):
    r = client.get("/health")

    assert r.status_code == 401


def test_health_bad_token(client):
    r = client.get(
        "/health",
        headers={"Authorization": "Bearer wrong"}
    )

    assert r.status_code == 401
