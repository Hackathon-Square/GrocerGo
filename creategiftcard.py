result = client.gift_cards.create_gift_card(
  body = {
    "idempotency_key": "001",
    "location_id": "LGM75327C41RJ",
    "gift_card": {
      "type": "DIGITAL",
      "gan_source": "SQUARE",
      "gan": "giftcard001"
    }
  }
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)