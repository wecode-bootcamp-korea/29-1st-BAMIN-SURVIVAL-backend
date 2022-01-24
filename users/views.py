import json
import bcrypt

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validator import *

class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            account        = data['account']
            nickname       = data['nickname']
            password       = data['password']
            email          = data['email']
            phone          = data['phone']

            is_password(password)
            is_email(email)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message':'E-MAIL ALREADY EXISTS'}, status = 400)
            if User.objects.filter(phone = phone).exists():
                return JsonResponse({'message':'PHONE-NUMBER ALREADY EXISTS'}, status=400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                account     = account,
                nickname    = nickname,
                password    = hashed_password,
                email       = email,
                phone       = phone
            )

            return JsonResponse({'message':'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)

