def test_create_payout(client, auth_headers):
    payload = {
        "amount": "2500",
        "currency": "EUR",
        "callback_url": "https://merchant/callback",
        "destination": {
            "type": "bank",
            "bank": {
                "iban": "NL91ABNA0417164300",
                "beneficiary_name": "Test User"
            }
        }
    }

    r = client.post("/v1/payout", json=payload, headers=auth_headers)

    assert r.status_code == 201
    assert r.json()["payout"]["amount"] == "2500"
