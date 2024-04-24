from django.db import models
from django.contrib.auth.models import AbstractUser
import json

# Create your models here.
class User(AbstractUser):
    giftcardids = models.JSONField(default=json.dumps(dict()), blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        pass

