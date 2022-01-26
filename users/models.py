from django.db import models

from core.models import Base

class User(Base):
    account        = models.CharField(max_length=50)
    nickname       = models.CharField(max_length=50)
    password       = models.CharField(max_length=200)
    email          = models.CharField(max_length=100, unique=True)
    phone          = models.CharField(max_length=20, unique=True)
    point          = models.IntegerField()

    class Meta:
        db_table = 'users'