from django.contrib import admin
from perfil.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'profesion', 'bio', 'birth_date')