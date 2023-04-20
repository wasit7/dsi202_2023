from django.urls import path
from .views import ProductDetailView, ProductListView
from .views import add_to_cart, order_summary

urlpatterns = [
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('order_summary', order_summary, name='order_summary')
]
