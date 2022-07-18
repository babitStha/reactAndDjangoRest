from itertools import product
from pickle import TRUE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    _id = models.AutoField(primary_key=True, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    user =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id =  models.AutoField(primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.createdAt)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    imageURL = models.CharField(max_length=200, null=True, blank=True)
    _id =  models.AutoField(primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact =models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id =  models.AutoField(primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.address)