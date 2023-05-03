from django.db import models
from menu.models import Menu
from personal_profile.models import User

# Create your models here.
class Order(models.Model):
    #vantar id
    #fær líka id frá Menu
    #fær id frá user
    pass

class Order_item(models.Model):
    #fær order item
    quantity = models.FloatField()


class Order_status(models.Model):
    #fær id frá menu
    #fær id frá order
    status = models.BooleanField()


class Payment(models.Model):
    #fær id frá order
    amount = models.FloatField()
    date = models.DateTimeField()