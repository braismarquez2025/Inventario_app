from import_export import resources
from producto.models import Proveedor

class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        fields = ('id', 'nombre')
