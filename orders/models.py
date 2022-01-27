from django.db import models

from core.models  import Base
from users.models import User

class Order(Base):
    order_number = models.IntegerField()
    users = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        db_table = 'orders'
