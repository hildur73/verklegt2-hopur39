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



