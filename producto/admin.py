from django.contrib import admin
from producto.resources import ProductoResource
from import_export.admin import ImportExportModelAdmin
from .models import Producto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource
    list_display = ('nombre', 'precio', 'categoria', 'proveedor', 'stock')