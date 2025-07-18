from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from movimientoStock.resources import MovimientosResource
from .models import MovimientoStock

# Register your models here.
@admin.register(MovimientoStock)
class MovimentosAdmin(ImportExportModelAdmin):
    resource_class = MovimientosResource
    list_display = ('producto_id', 'tipo', 'cantidad', 'fecha_hora')