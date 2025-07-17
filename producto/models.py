from django.db import models

from categoria.models import Categoria
from proveedor.models import Proveedor

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0) 
    stock_minimo = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.stock}"