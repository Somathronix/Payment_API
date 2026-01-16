import sys
import json
import hmac
import hashlib
import base64
import os


def sign(raw_body: bytes, secret: str) -> bytes:
    return hmac.new(
        secret.encode("utf-8"),
        raw_body,
        hashlib.sha256
    ).digest()


def main() -> None:
    """
    Usage:
      echo '{"test": 1}' | python sign_webhook.py
    or
      python sign_webhook.py file.json
    """

    secret = os.getenv("WEBHOOK_SECRET", "webhook_secret")

    # Read input
    if not sys.stdin.isatty():
        raw = sys.stdin.buffer.read()
    else:
        if len(sys.argv) < 2:
            print("Provide JSON via stdin or file path")
            sys.exit(1)

        with open(sys.argv[1], "rb") as f:
            raw = f.read()

    # Validate JSON
    try:
        json.loads(raw)
    except Exception:
        print("Input is not valid JSON")
        sys.exit(1)

    signature = sign(raw, secret)

    print("Secret:", secret)
    print("X-Signature (hex):", signature.hex())
    print("X-Signature (base64):", base64.b64encode(signature).decode())


if __name__ == "__main__":
    main()
