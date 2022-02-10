#!/bin/bash

echo -e "\033[0;32m데이터베이스 업데이트 중...\033[0m"

echo -e "\033[0;32카테고리 업데이트 중...\033[0m"
python db_categories.py
sleep 1
echo -e "\033[0;32m상품 업데이트 중...\033[0m"
python db_products.py
sleep 1
echo -e "\033[0;32m사이즈 업데이트 중...\033[0m"
python db_sizes.py
sleep 1
echo -e "\033[0;32m상품옵션 업데이트 중...\033[0m"
python db_product_options.py
sleep 1
echo -e "\033[0;32m이미지 업데이트 중...\033[0m"
python db_images.py
sleep 1

echo -e "\033[0;32m데이터베이스 업로드 완료!\033[0m"
