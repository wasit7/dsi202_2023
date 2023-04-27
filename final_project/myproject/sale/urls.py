from django.urls import path
from .views import ProductDetailView, ProductListView, OrderCreateView
from .views import add_to_cart

urlpatterns = [
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    # path('item_formset/', ItemFormSetView.as_view(), name='item_formset'),
    # path('order_summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
]
