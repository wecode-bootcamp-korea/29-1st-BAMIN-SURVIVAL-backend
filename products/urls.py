from django.urls    import path

from products.views import ProductDetailView, ProductListView, SlideImageView

urlpatterns = [
    path("",ProductListView.as_view()),
    path("/detail",ProductDetailView.as_view()),
    path("/slide",SlideImageView.as_view()),
]