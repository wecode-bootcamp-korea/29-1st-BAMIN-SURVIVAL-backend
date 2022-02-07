from django.db import models

from core.models     import Base
from users.models    import User
from products.models import ProductOption


class Cart(Base):
    quantity        = models.IntegerField(default = 0)
    user            = models.ForeignKey(User, on_delete = models.CASCADE)
    product_option  = models.ForeignKey(ProductOption, on_delete = models.CASCADE)

    class Meta:
        db_table = 'carts'