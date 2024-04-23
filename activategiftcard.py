result = client.gift_card_activities.create_gift_card_activity(
  body = {
    "idempotency_key": "100",
    "gift_card_activity": {
      "type": "ACTIVATE",
      "location_id": "LBAKXA7BAEKHX",
      "gift_card_gan": "001",
      "activate_activity_details": {
        "amount_money": {
          "amount": 20,
          "currency": "AUD"
        }
      }
    }
  }
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)