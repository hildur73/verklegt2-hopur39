from django.db import models

class User(models.Model):
    #vantar id hérna
    name = models.CharField(max_length=255)
    phone_number = models.FloatField()
    home_address = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class ProfileImages(models.Model):
    image = models.CharField(max_length=9999)
    user_name = models.ForeignKey(User, on_delete = models.CASCADE)


