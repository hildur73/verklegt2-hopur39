from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=9999)

class Menudetails(models.Model):
    description = models.CharField(max_length=255, blank=True)
    menuid = models.ForeignKey(Menu, on_delete=models.CASCADE)

