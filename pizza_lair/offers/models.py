from django.db import models
from menu.models import Menu
# Create your models here.
class Offers(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    pizza_id = models.ForeignKey(Menu, on_delete=models.CASCADE)