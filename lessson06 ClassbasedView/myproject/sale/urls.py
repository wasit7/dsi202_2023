from django.urls import path
from .views import ProductDetailView

urlpatterns = [
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]
