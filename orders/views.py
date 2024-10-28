from rest_framework import viewsets
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]