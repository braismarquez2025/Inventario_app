from django.db import models

from categoria.models import Categoria
from proveedor.models import Proveedor

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,  related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    stock = models.PositiveIntegerField() 
    stock_minimo = models.IntegerField(default=0)
    imagen = models.ImageField(null=True, blank=True)
    num_ventas = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"{self.nombre}"
    

    def stock_status(self):
        if self.stock <= self.stock_minimo:
            return "bajo"
        elif self.stock <= self.stock_minimo + 10:
            return "medio"
        return "alto"