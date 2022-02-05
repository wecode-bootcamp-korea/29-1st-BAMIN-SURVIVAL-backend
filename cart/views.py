import json

from django.views import View
from django.http import JsonResponse

from cart.models import Cart
from users.models import User
from users.utils import login_required

class CartView(View):
    @login_required
    def post (self, request):
        try:
            data = json.loads(request.body)
            user = request.user.id

            Cart.objects.create(
                users_id     = user,
                quantity     = data['quantity'],
                products_id  = data['products_id']
            )
            
            return JsonResponse({'message': 'SUCCESS', 'user_id' : user}, status = 200)

        except User.DoesNotExist:
            return JsonResponse({'message': 'USER_ID_DOES_NOT_EXIST'}, status = 400)
        except json.JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)