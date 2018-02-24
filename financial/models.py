from django.db import models
from django.utils import timezone


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    street = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=11)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=5)
    name = models.TextField()
    number_of_shares = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=None, decimal_places=2)
    date_purchased = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cryptocurrency(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    name = models.TextField()
    number_of_coins = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=None, decimal_places=2)
    date_purchased = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title