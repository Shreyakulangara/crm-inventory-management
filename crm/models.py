from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
