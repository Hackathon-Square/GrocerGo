from django.db import models

# Create your models here.


class Product(models.Model):
    Block = models.CharField(max_length=100)
    Shelf = models.CharField(max_length=100, null=True)
    Level = models.CharField(max_length=100, null=True)
    ProductName = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Unit = models.CharField(max_length=100)
    Stock = models.DecimalField(max_digits=10, decimal_places=2)
    ProductID = models.TextField()
    ProductPicPath = models.CharField(max_length=255)

    def __str__(self):
        return self.ProductName
