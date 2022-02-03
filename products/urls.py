from django.urls    import path

from products.views import ProductDetailView, CategoryView, ProductAllView

urlpatterns = [
    path("/<int:product_id>",ProductDetailView.as_view()),
    path("/all",ProductAllView.as_view()),
    path("/<str:category_name>", CategoryView.as_view()),
]