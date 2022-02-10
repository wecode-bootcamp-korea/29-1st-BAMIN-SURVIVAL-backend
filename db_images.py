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

PRODUCT_CSV_PATH = 'csv/images.csv'	# 3. csv 파일 경로
SLIDE_CSV_PATH   = 'csv/slide_images.csv'

def product_image_insert_products():
    with open(PRODUCT_CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            print(row)
            ProductImage.objects.create(
                image_url = row['image_url'],
                detail_image_url = row['detail_image_url'],
                product_id = row['product_id']
        )

    print('PRODUCT IMAGE DATA UPLOADED SUCCESSFULY!')

def slide_image_insert_products():
    with open(SLIDE_CSV_PATH, newline='', encoding='utf8') as csvfile:
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            print(row)
            SlideImage.objects.create(
                image_url = row['image_url']
        )

    print('SLIDE IMAGE DATA UPLOADED SUCCESSFULY!')

product_image_insert_products()
slide_image_insert_products()
