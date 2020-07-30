from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre de la categoría",
        help_text="Nombre de la categoría")

    icon = models.ImageField(
        null=True, blank=True, upload_to="categories",
        verbose_name="Icono de la categoría",
        help_text="Icono de la categoría")
    parent = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING,
        verbose_name="Categoría padre",
        help_text="Categoría padre")

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def _str_(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING,
        verbose_name="Categoría del servicio",
        help_text="Categoría del servicio")

    name = models.CharField(
        max_length=200,
        verbose_name="Nombre del servicio",
        help_text="Nombre del servicio")

    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción del servicio",
        help_text="Descripción del servicio")
    photo = models.ImageField(
        null=True, blank=True, upload_to="services",
        verbose_name="Foto del servicio",
        help_text="Foto del servicio")

    class Meta:
        ordering = ["name"]
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def _str_(self):
        return self.name