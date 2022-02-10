import json

from django.views     import View
from django.http      import JsonResponse

from cart.models     import Cart
from users.models    import User
from users.utils     import login_required

class CartView(View):
    @login_required
    def post (self, request):
        try:
            data              = json.loads(request.body)
            user              = request.user.id
            quantity          = data['quantity']
            product           = data['product_id']

            cart, created = Cart.objects.get_or_create(
                user_id            = user,
                quantity           = quantity,
                product_id  =  product,
                defaults = {'quantity': quantity}
            )

            if not created:
                cart.quantity += int(quantity)
                cart.save()
            
            current_total_cart = Cart.objects.filter(user_id = request.user.id).count()

            success_message = {
                'result' : {
                    'message' : 'SUCCESS',
                    'current_total_cart': current_total_cart
                }
            }
            return JsonResponse(success_message, status = 200)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'USER_ID_DOES_NOT_EXIST'}, status = 400)
        except KeyError as e:
            return JsonResponse({"message" : "KEY_ERROR: " + str(e).replace("'", '')}, status = 401)              
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)         

    @login_required
    def get (self, request):
        user   = request.user.id
        carts  = Cart.objects.filter(user_id = user)
        count  = carts.count()

        result = [
            {
                'cart_id'              : cart.id,
                'name'            : cart.product.name,
                'price'           : cart.product.price,
                'quantity'        : cart.quantity,
                'shipping'        : cart.product.shipping,
                'thumbnail_image' : cart.product.productimage_set.all()[0].image_url
            } for cart in carts ]

        return JsonResponse({
            'result' : result,
            'count'  : count
        }, status = 200)


    @login_required
    def patch (self, request, cart_id):
        try:
            data = json.loads(request.body)
            user = request.user.id
            cart = Cart.objects.get(id = cart_id, user_id = user)

            cart.quantity = data['quantity']
            cart.save()

            #current_total_cart = Cart.objects.filter(user_id = user).count()
            success_message = {
                'result' : {
                    'message' : 'SUCCESS'
                }
            }
            return JsonResponse(success_message, status = 200)

        except KeyError as e:
            return JsonResponse({"message" : "KEY_ERROR: " + str(e).replace("'", '')}, status = 401)
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)

    @login_required
    def delete (self, request):
        try:
            cart_ids = request.GET.getlist('cart_id', None)

            carts = Cart.objects.filter(id__in=cart_ids)

            if not carts:
                return JsonResponse({'message' : 'CART DOES NOT EXIST'})

            carts.delete()

            current_total_cart = Cart.objects.filter(user_id = request.user.id).count()
            success_message = {
                'result' : {
                    'message' : 'SUCCESS',
                    'current_total_cart': current_total_cart
                }
            }
            return JsonResponse(success_message, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)      
        except Cart.DoesNotExist:
            return JsonResponse({'message' : 'CART_DOSE_NOT_EXIST'}, status = 400)
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)