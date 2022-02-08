from django.urls    import path

from products.views import ProductDetailView, ProductListView

urlpatterns = [
    path("",ProductListView.as_view()),
    path("/detail",ProductDetailView.as_view())
]