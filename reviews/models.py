from django.db import models

from core.models     import Base
from users.models    import User
from products.models import Product

class Review(Base):
    star            = models.IntegerField()
    title           = models.CharField(max_length = 50)
    comment         = models.TextField()
    user            = models.ForeignKey(User, on_delete = models.CASCADE)
    product         = models.ForeignKey(Product, on_delete = models.CASCADE)

    class Meta:
        db_table = 'reviews'