from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Producto, Categoria, Proveedor

class ProductoResource(resources.ModelResource):
    categoria = fields.Field(
        column_name='categoria',
        attribute='categoria',
        widget=ForeignKeyWidget(Categoria, 'nombre')
    )
    proveedor = fields.Field(
        column_name='proveedor',
        attribute='proveedor',
        widget=ForeignKeyWidget(Proveedor, 'nombre')
    )

    class Meta:
        model = Producto
        import_id_fields = ('nombre',) 
        fields = ('nombre', 'precio', 'categoria', 'proveedor', 'stock')
