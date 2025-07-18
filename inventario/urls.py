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
from django.urls import path

from inventario.views import ProductoDeleteView, ProductosAllView, ProductoCreateView, ProductoDetailView, ProductoHistorialView, EntradaCreateView, SalidaCreateView, StockMinimoUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductosAllView.as_view(), name='productos_all'),
    path('add/', ProductoCreateView.as_view(), name='productos_add'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('producto/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('producto/<int:pk>/stock_minimo/', StockMinimoUpdateView.as_view(), name='stock_minimo_update'),
    path('producto/<int:pk>/movimientos/', ProductoHistorialView.as_view(), name='historial'),
    path('producto/<int:pk>/movimientos/nueva_entrada/',EntradaCreateView.as_view(), name='entrada_create'),
    path('producto/<int:pk>/movimientos/nueva_salida/',SalidaCreateView.as_view(), name='salida_create'),

]
