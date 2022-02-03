import json

from django.views import View
from django.http import JsonResponse

class CartView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)