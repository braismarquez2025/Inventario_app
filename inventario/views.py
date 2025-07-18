from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from categoria.models import Categoria
from inventario.forms import EntradaCreateForm, ProductoForm, SalidaCreateForm
from movimientoStock.models import MovimientoStock
from producto.models import Producto
from django.contrib import messages
from django.views.generic.edit import UpdateView


class ProductosAllView(ListView):
    model = Producto
    template_name = "productos/productos_all.html"
    context_object_name = "productos"

    def get_queryset(self):
        queryset = Producto.objects.all().select_related('categoria')
        categoria_id = self.request.GET.get('categoria')
        
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/productos_add.html"
    success_url = reverse_lazy("productos_all") 

    def form_valid(self, form):
        messages.success(self.request, 'Producto creado correctamente.')
        return super().form_valid(form)



class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock'] = self.object.stock
        return context
    

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_delete.html'
    success_url = reverse_lazy('productos_all') 

    def form_valid(self, form):
        messages.error(self.request, 'Producto eliminado correctamente.')
        return super().form_valid(form)

    

class ProductoHistorialView(DetailView):
    model = Producto
    template_name = 'stock/historial.html'
    context_object_name = 'movimientos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()

        entradas = producto.movimientos.filter(tipo='entrada')
        salidas = producto.movimientos.filter(tipo='salida')
        
        context['entradas'] = entradas
        context['salidas'] = salidas
        return context
    

class EntradaCreateView(CreateView):
    model = MovimientoStock
    form_class = EntradaCreateForm
    template_name = "stock/entrada_create.html" 

    def dispatch(self, request, *args, **kwargs):
        self.producto = get_object_or_404(Producto, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        movimiento = form.save(commit=False)
        movimiento.producto = self.producto  # Producto viene de la URL
        movimiento.tipo = "entrada"
        movimiento.save()

        # Actualiza stock
        self.producto.stock += movimiento.cantidad
        self.producto.save()

        return redirect('producto_detail', pk=self.producto.pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producto'] = self.producto
        return context


class SalidaCreateView(CreateView):
    model = MovimientoStock
    form_class = SalidaCreateForm
    template_name = "stock/salida_create.html" 

    def dispatch(self, request, *args, **kwargs):
        self.producto = get_object_or_404(Producto, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        cantidad_salida = form.cleaned_data['cantidad']

        if (self.producto.stock - cantidad_salida) < self.producto.stock_minimo:
            messages.add_message(self.request, messages.ERROR, 'Esta salida dejaría el stock por debajo del mínimo permitido.')
            return redirect('producto_detail', pk=self.producto.pk)


        movimiento = form.save(commit=False)
        movimiento.producto = self.producto  # Producto viene de la URL
        movimiento.tipo = "salida"
        movimiento.save()

        self.producto.stock -= cantidad_salida
        self.producto.save()
        messages.add_message(self.request, messages.SUCCESS, 'Salida registrada correctamente.')

        return redirect('producto_detail', pk=self.producto.pk)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producto'] = self.producto
        return context


class StockMinimoUpdateView(UpdateView):
    model = Producto
    template_name = "stock/stock_minimo_update.html"
    context_object_name = "producto" 
    fields = ['stock_minimo']

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Stock minimo actualizado.")
        return super(StockMinimoUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("producto_detail", kwargs={"pk": self.object.pk})