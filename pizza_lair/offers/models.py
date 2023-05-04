from django.db import models
from menu.models import Menu
# Create your models here.
class Offers(models.Model):
    description = models.CharField(max_length=255, blank=True)
    price = models.FloatField()

