from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
