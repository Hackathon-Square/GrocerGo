import os
from square.client import Client

client = Client(access_token=os.environ["SQUARE_ACCESS_TOKEN"], environment="production")

result = client.gift_cards.create_gift_card(
    body={
        "idempotency_key": "001",
        "location_id": "LGM75327C41RJ",
        "gift_card": {"type": "DIGITAL", "gan_source": "SQUARE"},
    }
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
