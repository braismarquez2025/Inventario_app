from django import forms
from django.contrib.auth.models import User
from perfil.models import UserProfile
from movimientoStock.models import MovimientoStock
from producto.models import Producto
from django.forms.widgets import ClearableFileInput

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'imagen', 'precio', 'categoria', 'proveedor', 'stock']


class EntradaCreateForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ['cantidad', 'fecha_hora']
        
        
class SalidaCreateForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ['cantidad', 'fecha_hora']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())

    terms = forms.BooleanField(
        required=True
    )
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'email',
            'password',
        ]
        help_texts = { 
            'username': None, 
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            UserProfile.objects.create(user=user)
        return user



class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(
        required=False,
        widget=ClearableFileInput(attrs={'class': 'd-none'}) 
    )

    eliminar_imagen = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput(),
    )
    
    class Meta:
        model = UserProfile
        fields = ["bio", "profesion", "telefono", "birth_date", "profile_picture", "pais"]

        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
            "profesion": forms.TextInput(),
            "telefono": forms.TextInput(),
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "profile_picture": ClearableFileInput(attrs={'class': 'd-none'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Nombre"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Apellidos"}),
            "email": forms.EmailInput(attrs={"placeholder": "Correo electrónico"}),
        }