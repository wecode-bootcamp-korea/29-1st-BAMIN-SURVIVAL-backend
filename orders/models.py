from django.db import models

from core.models import Base

class Order(Base):
    order_number = models.IntegerField()

    class Meta:
        db_table = 'orders'
