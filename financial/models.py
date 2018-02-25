from django.db import models
from django.utils import timezone


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=5)
    name = models.TextField()
    number_of_shares = models.IntegerField()
    purchase_price = models.FloatField()
    date_purchased = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)


class Cryptocurrency(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    name = models.TextField()
    number_of_coins = models.IntegerField()
    purchase_price = models.FloatField()
    date_purchased = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
