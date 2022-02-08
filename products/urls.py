from django.urls    import path

from products.views import ProductDetailView, CategoryListView, ProductListView 

urlpatterns = [
    path("/<int:product_id>",ProductDetailView.as_view()),
    path("",ProductListView.as_view()),
    path("/categories", CategoryListView.as_view()),
]
