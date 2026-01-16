def test_create_payin(client, auth_headers, payin_payload):
    r = client.post("/v1/payin", json=payin_payload, headers=auth_headers)

    assert r.status_code == 201
    data = r.json()

    assert data["payment"]["amount"] == "1000"
    assert data["payment"]["currency"] == "EUR"
    assert data["payment"]["status"] in ["pending", "succeeded"]


def test_get_payin(client, auth_headers, payin_payload):
    r = client.post("/v1/payin", json=payin_payload, headers=auth_headers)
    pid = r.json()["payment"]["id"]

    r2 = client.get(f"/v1/payin/{pid}", headers=auth_headers)

    assert r2.status_code == 200
    assert r2.json()["payment"]["id"] == pid


def test_cancel_payin(client, auth_headers, payin_payload):
    r = client.post("/v1/payin", json=payin_payload, headers=auth_headers)
    pid = r.json()["payment"]["id"]

    r2 = client.post(f"/v1/payin/{pid}/cancel", headers=auth_headers)

    assert r2.status_code == 200
    assert r2.json()["payment"]["status"] == "canceled"
