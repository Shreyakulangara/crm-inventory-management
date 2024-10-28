from django.urls import path
from .views import *

urlpatterns = [
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='customer-detail'),
    path('contacts/', ContactViewSet.as_view({'get': 'list', 'post': 'create'}), name='contact-list'),
]