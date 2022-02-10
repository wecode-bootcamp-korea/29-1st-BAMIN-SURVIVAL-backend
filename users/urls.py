from django.urls import path

from users.views import SignInView, SignUpView, CheckAccountView, CheckEmailView, CheckNicknameView, CheckPhoneView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/check-account', CheckAccountView.as_view()),
    path('/check-email', CheckEmailView.as_view()),
    path('/check-nickname', CheckNicknameView.as_view()),
    path('/check-phone', CheckPhoneView.as_view())
]