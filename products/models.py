from django.db import models

from core.models import Base

class Category(Base):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'categories'

class ProductOption(Base):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    size    = models.ForeignKey('Size', on_delete = models.CASCADE, null=True)

    class Meta:
        db_table = 'product_options'

class Product(Base):
    category       = models.ForeignKey('Category', on_delete = models.CASCADE)
    name           = models.CharField(max_length = 50)
    shipping       = models.CharField(max_length = 10)
    price          = models.PositiveIntegerField()
    discount_rate  = models.PositiveSmallIntegerField(null = True)
    discount_price = models.PositiveIntegerField(null = True)
    is_green       = models.BooleanField(default = False)
    is_sale        = models.BooleanField(default = False)
    stock          = models.PositiveSmallIntegerField(null = True)

    class Meta:
        db_table = 'products'

class Image(Base):
    img_url = models.URLField(max_length = 200)
    product = models.ForeignKey('Product', on_delete = models.CASCADE)

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name = models.CharField(max_length = 5)

    class Meta:
        db_table = 'sizes'
