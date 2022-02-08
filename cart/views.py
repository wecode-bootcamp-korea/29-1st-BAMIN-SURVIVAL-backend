import json

from django.views     import View
from django.http      import JsonResponse

from cart.models     import Cart
from users.models    import User
from products.models import ProductOption
from users.utils     import login_required

# product option 도 넣어줘야함.
class CartView(View):
    @login_required
    def post (self, request):
        try:
            data              = json.loads(request.body)
            user              = request.user
            quantity          = data['quantity']
            product_option_id = data['product_option_id']

            cart, created     = Cart.objects.get_or_create(
                user              = user,
                product_option_id = product_option_id,
                defaults = {}
            )

            if not created:
                cart.quantity += quantity
                cart.save()

#             cart = Cart.objects.create(
#                 users_id     = request.user.id,
#                 products_id  = data['products_id']
#             )
            # quantity 수량 연산 식 써줘야합니다

            current_total_cart = Cart.objects.filter(users_id=request.user.id).count()

            success_message = {
                'result' : {
                    'message' : 'SUCCESS',
                    'current_total_cart': current_total_cart
                }
            }
            # users_id 가 생기면 카운트
            # 임시 메시지
            return JsonResponse(success_message, status = 200)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'USER_ID_DOES_NOT_EXIST'}, status = 400)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)               
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)         

    @login_required
    def get (self, request):
        # products 조회 후 quantity 도 넣어줘야합니다.
        # 수정 중
        user   = request.user
        carts  = Cart.objects.filter(user = user)
        count  = carts.count()

        result = [
            {
                'name'           : cart.product.name,
                'price'          : item.products.price,
                #'options'        : #옵션 넣어야함
                'quantity'       : item.quantity,
                'shipping'       : item.products.shipping,
                'thumbnail_img'  : item.products.image_set.all()[0].img_url
            } for cart in carts ]
        return JsonResponse({
            'result' : result,
            'count'  : count
        }, status = 200)

    @login_required
    def patch (self, request):
        try:
            data = json.loads(request.body)
            cart = Cart.objects.get(id = data['cart_id'])
            #옵션 들어가야함
            cart.quantity = data['quantity']
            cart.save()

            current_total_cart = Cart.objects.filter(users_id=request.user.id).count()
            success_message = {
                'result' : {
                    'message' : 'SUCCESS',
                    'current_total_cart': current_total_cart
                }
            }
            return JsonResponse(success_message, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)

    @login_required
    def delete (self, request):
        try:
            # :8000/cart?cart_id=1&cart_id=2&cart_id=3
            cart_ids = request.GET.getlist(cart_id, None)
            # cart_ids = [1, 2, 3]

            carts = Cart.objects.filter(id__in=cart_ids)

            if not carts:
                return JsonResponse({'message' : 'CART DOES NOT EXIST'})

            carts.delete()

#             data = json.loads(request.body)
#             Cart.objects.get(id = data['cart_id']).delete()
            #옵션 들어가야하는지.
#             current_total_cart = Cart.objects.filter(users_id=request.user.id).count()
            success_message = {
                'result' : {
                    'message' : 'SUCCESS'
#                     'current_total_cart': current_total_cart
                }
            }
            return JsonResponse(success_message, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)      
        except Cart.DoesNotExist:
            return JsonResponse({'message' : 'CART_DOSE_NOT_EXIST'}, status = 400)
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)
