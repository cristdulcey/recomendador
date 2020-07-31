from django.db import models

from persons.models import Supervisor,City,Client
from services.models import Services


class Company(models.Model):
    name = models.CharField(max_length=255)
    nit = models.BigIntegerField()
    logo = models.ImageField(upload_to="shop_image", null=True, blank=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Compañia"
        verbose_name_plural = "Compañias"

    def __str__(self):
        return self.name

class BranchCompany (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    geolocation =models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    schedule = models.TextField()

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.company.name

class BranchServices (models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    branch_company = models.ForeignKey(BranchCompany, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
      verbose_name = "Rama Servicio"
      verbose_name_plural = "Rama Servicios"

    def __str__(self):
        return self.branch_company.company.name

class Qualification (models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True)
    comment = models.TextField(max_length=255)
    branch_services = models.ForeignKey(BranchServices, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "califacion"
        verbose_name_plural = "calificaciones"

    def __str__(self):
        return self.comment



