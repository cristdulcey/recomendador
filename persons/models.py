from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.name

class Client(models.Model):
    phone = models.BigIntegerField()
    address = models.CharField(max_length=255, blank=True)
    geolocation = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.user.username

class Supervisor (models.Model):
    phone = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisores"

    def __str__(self):
        return self.user.username