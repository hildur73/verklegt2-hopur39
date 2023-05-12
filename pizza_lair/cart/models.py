from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu


# Create your models here.
class Cart(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    payment = models.BooleanField()


class CartItem(models.Model):
    cartid = models.ForeignKey(Cart, on_delete=models.CASCADE)
    menuid = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Checkout(models.Model):
    fullname = models.CharField(max_length=255)
    streetname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    postalcode = models.IntegerField()


class Paymentstep(models.Model):
    cardholder = models.CharField(max_length=255)
    cardnumber = models.IntegerField()
    expirationdate = models.DateField()
    cvc = models.IntegerField()


