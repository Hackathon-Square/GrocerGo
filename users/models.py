from django.db import models
from django.contrib.auth.models import AbstractUser
import json

# Create your models here.
class User(AbstractUser):
    giftcardids = models.JSONField(default=json.dumps(dict()), blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        pass


class Product(models.Model):
    Block = models.CharField(max_length=100)
    Shelf = models.CharField(max_length=100, null=True)
    Level = models.CharField(max_length=100, null=True)
    ProductName = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Unit = models.CharField(max_length=100)
    Stock = models.DecimalField(max_digits=10, decimal_places=2)
    ProductID = models.TextField()
    ProductPicPath = models.CharField(max_length=255, default="", null=True)

    def __str__(self):
        return self.ProductName
