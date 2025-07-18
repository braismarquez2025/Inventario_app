from import_export import resources
from producto.models import Categoria

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')
