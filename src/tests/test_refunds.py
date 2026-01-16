def test_create_refund(client, auth_headers, payin_payload):
    # create payin
    r = client.post("/v1/payin", json=payin_payload, headers=auth_headers)
    pid = r.json()["payment"]["id"]

    payload = {"amount": "500"}

    r2 = client.post(
        f"/v1/payin/{pid}/refunds",
        json=payload,
        headers=auth_headers
    )

    assert r2.status_code == 201
    assert r2.json()["refund"]["amount"] == "500"
