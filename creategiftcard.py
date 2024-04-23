result = client.gift_cards.create_gift_card(
  body = {
    "idempotency_key": "100",
    "location_id": "LBAKXA7BAEKHX",
    "gift_card": {
      "type": "DIGITAL",
      "gan_source": "SQUARE",
      "gan": "001"
    }
  }
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)