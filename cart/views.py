import json

from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from cart.models import Cart
from products.models import Product
from users.models import User
from users.utils import login_required

class CartView(View):
    @login_required
    def post (self, request):
        try:
            data = json.loads(request.body)
            user = request.user.id
            Cart.objects.create(
                users_id = user,
                quantity = data['quantity'],
                products_id  = Product.objects.get(id=data['product'])
            )
            return JsonResponse({'message': 'SUCCESS', 'user' : user}, status=200)
        except KeyError as k:
            return JsonResponse({'message': k}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User id Does Not Exist'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'Product id Does Not Exist'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSONDECODE_ERROR'}, status = 400)