from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()


class Menu_details(models.Model):
    description = models.CharField(max_length=255, blank=True)
    pizza_id = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Menu_image(models.Model):
    pizza_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)