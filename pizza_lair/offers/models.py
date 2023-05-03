from django.db import models
from menu.models import Menu
# Create your models here.
class Offers(models.Model):
    #vantar id
    name = models.CharField(max_length=255)
    price = models.FloatField()
    #fær líka id frá Menu