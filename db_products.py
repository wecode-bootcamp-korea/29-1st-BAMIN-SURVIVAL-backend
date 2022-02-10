import csv
import os
import sys
import django

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baemin.settings")	# 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

from products.models import *	# 2. App이름.models

CSV_PATH = 'csv/products.csv'	# 3. csv 파일 경로

def insert_products():
    with open(CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            print(row)
            # name,price,discount_price,discount_rate,shipping,category_id
            Product.objects.create(
                name           = row['name'],
                price          = row['price'],
                discount_price = row['discount_price'],
                discount_rate  = row['discount_rate'],
                shipping       = row['shipping'],
                is_green       = row['is_green'],
                is_sale        = row['is_sale'],
                stock          = row['stock'],
                product_option = row['product_option'],
                category_id    = row['category_id']
        )

    print('DATA UPLOADED SUCCESSFULY!')

insert_products()
