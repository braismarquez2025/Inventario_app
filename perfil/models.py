from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    profesion = models.CharField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(verbose_name="Fecha de nacimiento", null=True, blank=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Perfil',
        verbose_name_plural = 'Perfiles'