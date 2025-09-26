from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="Apellido")
    email = models.EmailField(blank=True, verbose_name="Email")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Avatar")
    biography = models.TextField(max_length=500, blank=True, verbose_name="Biografía")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return f"Perfil de {self.user.username}"