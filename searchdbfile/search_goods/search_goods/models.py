from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    block = models.CharField(max_length=7, null=True, blank=True, db_column='Block')
    shelf = models.CharField(max_length=1, null=True, blank=True, db_column='Shelf')
    level = models.CharField(max_length=7, null=True, blank=True, db_column='Level')
    product_name = models.CharField(max_length=42, null=True, blank=True, db_column='ProductName')
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, db_column='Price')
    unit = models.CharField(max_length=5, null=True, blank=True, db_column='Unit')
    stock = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, db_column='Stock')
    product_id = models.CharField(max_length=36, null=True, blank=True, db_column='ProductID')
    product_pic_path = models.CharField(max_length=62, null=True, blank=True, db_column='ProductPicPath')

    class Meta:
        db_table = 'Products'  # 确保表名匹配

    def __str__(self):
        return self.product_name
