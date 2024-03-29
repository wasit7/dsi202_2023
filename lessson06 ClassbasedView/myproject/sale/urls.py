from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
]
