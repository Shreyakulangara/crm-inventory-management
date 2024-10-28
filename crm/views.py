from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer, ContactSerializer
from .models import Customer, Contact
from rest_framework.permissions import IsAuthenticated


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]