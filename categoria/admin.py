from django.contrib import admin
from categoria.resources import CategoriaResource
from import_export.admin import ImportExportModelAdmin
from .models import Categoria

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin):
    resource_class = CategoriaResource
    list_display = ('id', 'nombre')