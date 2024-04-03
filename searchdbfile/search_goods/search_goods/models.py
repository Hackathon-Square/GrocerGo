from django.db import models

class Product(models.Model):
    block = models.TextField(null=True, blank=True)
    shelf = models.TextField(null=True, blank=True)
    level = models.TextField(null=True, blank=True)
    ProductName = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'try_products'

    def __str__(self):
        return self.ProductName