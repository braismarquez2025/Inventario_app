from django import forms

from movimientoStock.models import MovimientoStock
from producto.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria']


class EntradaCreateForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ['cantidad', 'fecha_hora']
        
        
class SalidaCreateForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ['cantidad', 'fecha_hora']