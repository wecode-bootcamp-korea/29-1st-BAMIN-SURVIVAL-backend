import json
import bcrypt
import jwt

from django.http            import JsonResponse
from django.views           import View
from django.conf            import settings
from django.core.exceptions import ValidationError

from users.models    import User
from users.validator import email_validation, password_validation

class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            account       = data['account']
            nickname      = data['nickname']
            password      = data['password']
            email         = data['email']
            phone         = data['phone']

            email_validation(email)
            password_validation(password)

            if User.objects.filter(account=account).exists():
                return JsonResponse({'message':'ACCOUNT ALREADY EXISTS'}, status = 400)
            if User.objects.filter(nickname=nickname).exists():
                return JsonResponse({'message':'NICKNAME ALREADY EXISTS'}, status = 400)
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
                phone       = phone,
                point       = 1000000
            ) 
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        except ValidationError as e:
            return JsonResponse({'message' : e.message}, status = 400)

class SignInView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            password = data['password']
            user     = User.objects.get(account = data['account'])

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

            token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, settings.ALGORITHM)

            users = User.objects.get(id = user.id)
            result= {
                'nickname' : users.nickname,
                'point'    : users.point
            }
            success_message = {
                'SUCCESS' : {
                    'ACCESS_TOKEN' : token,
                    'RESULT' : result
                }
            }

            return JsonResponse(success_message, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'DOES NOT EXIST USER'}, status = 400)