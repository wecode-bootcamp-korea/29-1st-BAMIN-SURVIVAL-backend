import jwt

from django.conf  import settings
from django.http  import JsonResponse

from users.models import User

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization')
            payload  = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id = payload['users_id'])
        
        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({'message': 'USER_DOES_NOT_EXIST'}, status = 400)

        return func(self, request, *args, **kwargs)   

    return wrapper