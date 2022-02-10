from django.urls    import path

from cart.views import CartView

urlpatterns = [
    path('',CartView.as_view()),
    path('/<int:cart_id>',CartView.as_view())
]