from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=9999)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

