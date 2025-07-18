from django.db import models

from producto.models import Producto
from django.utils import timezone

# Create your models here.
class MovimientoStock(models.Model):
    ENTRADA = 'entrada'
    SALIDA = 'salida'

    TIPO_MOVIMIENTO_CHOICES = [
        (ENTRADA, 'Entrada'),
        (SALIDA, 'Salida'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="movimientos")
    tipo = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO_CHOICES)
    cantidad = models.PositiveIntegerField()
    fecha_hora = models.DateTimeField(default=timezone.now)
