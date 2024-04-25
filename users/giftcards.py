def activate_gift_card(client):
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

    return result


def create_gift_card(client):
    result = client.gift_cards.create_gift_card(
        body={
            "idempotency_key": "001",
            "location_id": "LGM75327C41RJ",
            "gift_card": {"type": "DIGITAL", "gan_source": "SQUARE", "gan": "giftcard001"},
        }
    )

    return result
