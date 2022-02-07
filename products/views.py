from django.views       import View
from django.http        import JsonResponse
from django.db.models   import Q

from products.models    import Product, Category

class ProductListView(View):
    def get(self, request):
        try:
            limit    = int(request.GET.get('limit' , 16))
            offset   = int(request.GET.get('offset', 0))
            category = request.GET.get('category', None)

            q = Q()

            if category:
                q &= Q(category__name = category)

            products = Product.objects.filter(q)[offset : offset+limit]
            result = [{
                'id'             : product.id,
                'name'           : product.name,
                'shipping'       : product.shipping,
                'price'          : product.price,
                'discount_price' : product.discount_price,
                'is_green'       : product.is_green,
                'is_sale'        : product.is_sale,
                'stock'          : product.stock,
                'category_name'  : product.category.name,
                'thumbnail_image': [image.img_url for image in product.image_set.all()]
            }for product in products]

            return JsonResponse({'message':result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({'message' : 'PRODUCT_DOES_NOT_EXIST'}, status = 400)

        except AttributeError:
            return JsonResponse({'message' : 'ATTRIBUTE_ERROR'}, status = 400)

        except TypeError:
            return JsonResponse({'message' : 'TYPE_ERROR'}, status = 400)

class ProductDetailView(View):
    def get(self, request):
        try:
            product_id = request.GET.get('id' , None)

            product = Product.objects.get(id = product_id)
            result = {
                'id'              : product.id,
                'name'            : product.name,
                'shipping'        : product.shipping,
                'price'           : product.price,
                'discount_price'  : product.discount_price,
                'is_green'        : product.is_green,
                'is_sale'         : product.is_sale,
                'stock'           : product.stock,
                'category_name'   : product.category.name,
                'thumbnail_image' : [image.img_url for image in product.image_set.all()],
                'detail_image'    : [image.detail_img_url for image in product.image_set.all()]
            }

            return JsonResponse({'result': result}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({"message" : "INVALID_PRODUCT"}, status = 404)