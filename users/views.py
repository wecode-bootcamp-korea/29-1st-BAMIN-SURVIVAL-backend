import Json
import bcrypt
import jwt

from json.decoder           import JSONDecodeError
from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View

 from users.models import User
 from my_settings  import SECRET_KEY, ALGORITHM


class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            id = data["id"]
            password = data["password"].encode("utf-8")
            user = User.objects.get(id=id)

            if not bcrypt.checkpw(password, user.password.encode(‘utf-8’)):
                return JsonResponse({“message”: “INVALID_USER”}, status=400)

            access_token = jwt.encode({"id": id} SECRET_KEY, ALGORITHM)

            return JsonResponse({"access_token": access_token}, status=200)

        except JSONDecodeError:
            return JsonResponse({"message": "INVALID_JSON"}, status=400)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

        except ValidationError:
            return JsonResponse({"message": "INVALID_USER"}, status=400)
