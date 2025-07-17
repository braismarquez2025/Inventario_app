from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from proveedor.resources import ProveedorResource
from .models import Proveedor

# Register your models here.
@admin.register(Proveedor)
class ProveedorAdmin(ImportExportModelAdmin):
    resource_class = ProveedorResource
    list_display = ('id', 'nombre')