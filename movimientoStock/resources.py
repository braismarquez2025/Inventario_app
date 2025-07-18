from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import MovimientoStock, Producto
from import_export.widgets import DateTimeWidget

class MovimientosResource(resources.ModelResource):
    producto = fields.Field(
        column_name='producto',
        attribute='producto',
        widget=ForeignKeyWidget(Producto, 'id')
    )
    fecha_hora = fields.Field(
        column_name='fecha_hora',
        attribute='fecha_hora',
        widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S')
    )
    class Meta:
        model = MovimientoStock
        fields = ('producto', 'tipo', 'cantidad', 'fecha_hora')
        import_id_fields = []
