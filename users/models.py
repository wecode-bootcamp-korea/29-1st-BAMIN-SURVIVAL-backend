from django.db import models

class User(models.Model):
    account        = models.CharField(max_length=50)
    nickname       = models.CharField(max_length=50)
    password       = models.CharField(max_length=200)
    email          = models.CharField(max_length=100, unique=True)
    phone          = models.CharField(max_length=20, unique=True)
    point          = models.IntegerField()
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'