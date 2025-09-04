"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from inventario.views import EntradaCreateView, RegisterView, SalidaCreateView, ModificarStockView, ProductoCreateView, ProductoDeleteView, ProductoDetailView, HomeView, MovimientosView, lista_productos, LoginView, LogoutView, TerminosView, editar_perfil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view() ,name="login"),
    path('logout/', LogoutView ,name="logout"),
    path('terminos/', TerminosView.as_view() ,name="terminos"),
    path('perfil/', editar_perfil, name="perfil"),
    path('productos/', lista_productos, name='productos_all'),
    path('movimientos/', MovimientosView.as_view(), name='movimientos'),
    path('producto/add/', ProductoCreateView.as_view(), name='productos_add'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('producto/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('producto/<int:pk>/manage_stock/', ModificarStockView.as_view(), name='modificar_stock'),
    path('producto/<int:pk>/manage_stock/add/', EntradaCreateView.as_view(), name='add_stock'),
    path('producto/<int:pk>/manage_stock/delete/', SalidaCreateView.as_view(), name='delete_stock'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
