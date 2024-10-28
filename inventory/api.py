from django.urls import path
from .views import ProductViewSet, StockViewSet

urlpatterns = [
    # Product URLs
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
    
    # Stock URLs
    path('stocks/', StockViewSet.as_view({'get': 'list', 'post': 'create'}), name='stock-list'),
    path('stocks/<int:pk>/', StockViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='stock-detail'),
]
