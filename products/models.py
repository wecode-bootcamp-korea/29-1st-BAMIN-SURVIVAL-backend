from django.db import models

from core.models import Base

class Category(Base):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'categories'

class ProductOptions(Base):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    price   = models.PositiveIntegerField()
    size    = models.CharField(max_length = 5)
    color   = models.CharField(max_length = 10)
    option  = models.CharField(max_length = 30)
    agency  = models.CharField(max_length = 10)

class Product(Base):
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    name     = models.CharField(max_length = 50)
    shipping = models.CharField(max_length = 10)

class Image(Base):
    url     = models.URLField(max_length = 200)
    product = models.ForeignKey('Product', on_delete = models.CASCADE)

    class Meta:
        db_table = 'images'
