import os
from square.client import Client

client = Client(access_token=os.environ["SQUARE_ACCESS_TOKEN"], environment="production")

result = client.gift_card_activities.create_gift_card_activity(
    body={
        "idempotency_key": "001",
        "gift_card_activity": {
            "type": "ACTIVATE",
            "location_id": "LGM75327C41RJ",
            "gift_card_id": "gftc:2bcda6a90d524a6db268bbd72c82966a",
            "gift_card_gan": "7783324663378794",
            "activate_activity_details": {
                "amount_money": {"amount": 20, "currency": "AUD"},
                "buyer_payment_instrument_ids": ["first"],
            },
        },
    }
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
