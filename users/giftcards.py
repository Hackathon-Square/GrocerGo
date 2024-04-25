import json
from .models import User


def activate_gift_card(client, customer_email):
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

    user = User.objects.get(email=customer_email)
    giftcardids = json.loads(user.giftcardids)
    ids = giftcardids.get("ids", [])
    ids.append(result["body"]["gift_card_activity"]["gift_card_id"])
    giftcardids["ids"] = ids
    user.giftcardids = giftcardids
    user.balance += result["body"]["gift_card_activity"]["activate_activity_details"]["amount_money"]["amount"]
    user.save()

    return result


def create_gift_card(client):
    result = client.gift_cards.create_gift_card(
        body={
            "idempotency_key": "001",
            "location_id": "LGM75327C41RJ",
            "gift_card": {
                "type": "DIGITAL",
                "gan_source": "SQUARE",
                "gan": "giftcard001",
            },
        }
    )

    return result
