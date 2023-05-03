from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    #vantar id

class Menu_details(models.Model):
    description = models.CharField(max_length=255, blank=True)
    #fær id fra Menu
    #þarf stærð hér?
