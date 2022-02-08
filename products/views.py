from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from products.models import Product, Category

class ProductListView(View):
    def get(self, request):
        try:
            # QueryDict
            # :8000/product?limit=20&offset=0
            limit       = request.GET.get('limit', 20)
            offset      = request.GET.get('offset', 0)
            category = int(request.GET.get('category', None))
            sort        = request.GET.get('sort', '-created_at')

            q = Q()

            if category:
                q &= Q(category__name = category)

            products = Product.objects.filter(q)\
                                      .order_by(sort)[offset : offset+limit]

            result = [{

            } for product in products ]

            return JsonResponse({'message' : result}, status=200)

#             alls = Product.objects.all()
#             result = [
#                 {
#                     'id'             : all.id,
#                     'name'           : all.name,
#                     'shipping'       : all.shipping,
#                     'price'          : all.price,
#                     'is_green'       : all.is_green,
#                     'is_sale'        : all.is_sale,
#                     'category_id'    : all.category_id,
#                     'stock'          : all.stock,
#                     'discount_price' : all.discount_price,
#                     'thumbnail_image': [image.img_url for image in all.image_set.all()]
#                     }for all in alls]
# 
#             return JsonResponse({'result': result}, status = 200) 
#         
        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_DOES_NOT_EXIST'}, status = 400)

        except AttributeError:
            return JsonResponse({'message' : 'ATTRIBUTE_ERROR'}, status = 400)
        
        except TypeError:
            return JsonResponse({'message' : 'TYPE_ERROR'}, status = 400)

class CategoryListView(View):
    # :8000/products/categories
    def get(self, request):
        categories = Category.objects.all()

        results = [{
            'id'   : category.id,
            'name' : category.name
        } for category in categories]

        return JsonResponse({...})

# class CategoryView(View):
#     def get(self, request, category_name):
#         try:
#             category_name = Category.objects.get(name = category_name)
#             category_data = Product.objects.filter(category_id = category_name.id)
#             result = [
#                 {
#                     'id'             : category_item.id,
#                     'name'           : category_item.name,
#                     'shipping'       : category_item.shipping,
#                     'price'          : category_item.price,
#                     'is_green'       : category_item.is_green,
#                     'is_sale'        : category_item.is_sale,
#                     'category_id'    : category_item.category_id,
#                     'stock'          : category_item.stock,
#                     'discount_price' : category_item.discount_price,
#                     'thumbnail_image': [image.img_url for image in category_item.image_set.all()]
#                     }for category_item in category_data]
# 
#             return JsonResponse({'result' : result}, status = 200)
# 
#         except Category.DoesNotExist:
#             return JsonResponse({'message' : 'CATEGORY_DOES_NOT_EXIST'}, status = 400)
# 
#         except AttributeError:
#             return JsonResponse({'message' : 'ATTRIBUTE_ERROR'}, status = 400)
#         
#         except TypeError:
#             return JsonResponse({'message' : 'TYPE_ERROR'}, status = 400)   

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id = product_id)
            result = {
                'id'              : product.id,
                'name'            : product.name,
                'shipping'        : product.shipping,
                'price'           : product.price,
                'is_green'        : product.is_green,
                'is_sale'         : product.is_sale,
                'category_id'     : product.category_id,
                'stock'           : product.stock,
                'discount_price'  : product.discount_price,
                'thumbnail_image' : product.image_set.all()[0].img_url,
                'detail_image'    : product.image_set.all()[0].detail_img_url

            }

            return JsonResponse({'result': result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status = 404)
