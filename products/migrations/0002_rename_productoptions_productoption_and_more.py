# Generated by Django 4.0.1 on 2022-01-27 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductOptions',
            new_name='ProductOption',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
        migrations.AlterModelTable(
            name='productoption',
            table='product_options',
        ),
    ]
