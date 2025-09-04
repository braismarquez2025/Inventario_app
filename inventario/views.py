from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, FormView, TemplateView, UpdateView
from django.urls import reverse, reverse_lazy
from categoria.models import Categoria
from inventario.forms import EntradaCreateForm, LoginForm, ProductoForm, RegistrationForm, SalidaCreateForm, UserForm, UserProfileForm
from perfil.models import UserProfile
from proveedor.models import Proveedor
from movimientoStock.models import MovimientoStock
from producto.models import Producto
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect




class HomeView(ListView):
    model = MovimientoStock
    template_name = "general/home.html"
    context_object_name = "movimientos"

    def get_queryset(self):
        return MovimientoStock.objects.all().order_by("-fecha_hora")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Tambien le pasamos todos los productos por context
        context['productos'] = Producto.objects.all().order_by("-num_ventas")[:5]
        context['entradas'] = MovimientoStock.objects.all().filter(tipo='entrada')[:5]
        context['salidas'] = MovimientoStock.objects.all().filter(tipo='salida')[:5]
        return context

    
@login_required
def lista_productos(request):
    orden = request.GET.get("orden", "categoria")
    
    if orden == "proveedor":
        grupos = Proveedor.objects.prefetch_related("productos").all()
    else:
        grupos = Categoria.objects.prefetch_related("productos").all()
    
    return render(request, "productos/productos_all.html", {
        "grupos": grupos,
        "orden": orden,
    })
    


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/productos_add.html"
    success_url = reverse_lazy("productos_all") 

    def form_valid(self, form):
        messages.success(self.request, 'Producto creado correctamente')
        return super().form_valid(form)



class ProductoDetailView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'
    context_object_name = 'producto'



class MovimientosView(LoginRequiredMixin, ListView):
    model = MovimientoStock
    template_name = 'movimientos/movimientos.html'
    context_object_name = 'movimientos'

    def get_queryset(self):
        return MovimientoStock.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movimientos = self.get_queryset()

        entradas = movimientos.filter(tipo='entrada').order_by('-fecha_hora')
        salidas = movimientos.filter(tipo='salida').order_by('-fecha_hora')

        todos = list(entradas) + list(salidas)
        todos.sort(key=lambda m: m.fecha_hora, reverse=True)
        
        context['entradas'] = entradas
        context['salidas'] = salidas
        context['todos'] = todos
        return context



class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/producto_delete.html'
    success_url = reverse_lazy('producto_detail') 

    def form_valid(self, form):
        messages.error(self.request, 'Producto eliminado correctamente.')
        return super().form_valid(form)

    

class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = MovimientoStock
    form_class = EntradaCreateForm
    template_name = "stock/add_stock.html" 

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

        messages.success(self.request, 'Entrada realizada con éxito.')

        return redirect('producto_detail', pk=self.producto.pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producto'] = self.producto
        return context



class SalidaCreateView(LoginRequiredMixin, CreateView):
    model = MovimientoStock
    form_class = SalidaCreateForm
    template_name = "stock/delete_stock.html" 

    def dispatch(self, request, *args, **kwargs):
        self.producto = get_object_or_404(Producto, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        cantidad_salida = form.cleaned_data['cantidad']

        if (self.producto.stock - cantidad_salida) < self.producto.stock_minimo:
            messages.add_message(self.request, messages.ERROR, 'Esta salida dejaría el stock por debajo del mínimo permitido.')
            return redirect('producto_detail', pk=self.producto.pk)


        movimiento = form.save(commit=False)
        movimiento.producto = self.producto 
        movimiento.tipo = "salida"
        movimiento.save()

        self.producto.stock -= cantidad_salida
        self.producto.save()
        messages.success(self.request, 'Salida realizada con éxito.')

        return redirect('producto_detail', pk=self.producto.pk)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producto'] = self.producto
        return context
    


class ModificarStockView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "stock/modificar_stock.html"
    context_object_name = "producto"



class RegisterView(CreateView):
    template_name = "general/register.html"
    model = User
    success_url = reverse_lazy('home')
    form_class = RegistrationForm


    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente")
        return super(RegisterView, self).form_valid(form)
    


class LoginView(FormView):
    template_name = "general/login.html"
    form_class = LoginForm

    # Dado un user y una contraseña nos va a devolver si está autenticado o no
    def form_valid(self, form):
        usuario = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=usuario, password=password)

        #Si el usuario está ok, lo logueas y lo rediriges a la home
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f'Bienvenido de nuevo {user.username}')
            return HttpResponseRedirect(reverse('home'))
        
        else:
            messages.add_message(self.request, messages.ERROR, 'Usuario no válido o contraseña incorrecta')
            return super(LoginView, self).form_invalid(form)


@login_required
def LogoutView(request):
    logout(request)
    messages.add_message(request, messages.INFO, f'Se ha cerrado la sesión correctamente')
    return HttpResponseRedirect(reverse('home'))



class TerminosView(TemplateView):
    template_name = "general/terminos.html"



class MiPerfilView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = "general/perfil.html"
    context_object_name = "perfil"



@login_required
def editar_perfil(request):
    user = request.user
    perfil = user.profile

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("perfil")
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=perfil)

    return render(request, "general/perfil.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "perfil": perfil,
    })










