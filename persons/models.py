from django.contrib.auth.models import User
from django.db import models
from geoposition.fields import GeopositionField
# Create your models here.
from geoposition.fields import GeopositionField


class City(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    geolocation = GeopositionField()


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.user.username

class Supervisor (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone = models.BigIntegerField()



    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisores"

    def __str__(self):
        return self.user.username