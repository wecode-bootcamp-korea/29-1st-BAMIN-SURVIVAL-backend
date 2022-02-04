import json

from django.views import View
from django.http import JsonResponse

from cart.models import Cart
from users.models import User

class CartView(View):
    def post(self, request): 
        data       = json.loads(request.body)
        user           = User.objects.get(id=request.users.id)
        quantity   = data['quantity']
        print(user)
        print(quantity)