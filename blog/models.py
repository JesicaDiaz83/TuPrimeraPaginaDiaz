from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Autor(models.Model):
    """Modelo para representar autores del blog"""
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    biografia = models.TextField(max_length=500, blank=True, verbose_name="Biografía")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Post(models.Model):
    """Modelo para representar publicaciones del blog"""
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    publicado = models.BooleanField(default=True, verbose_name="Publicado")
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-fecha_creacion']
        
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    """Modelo para representar comentarios en las publicaciones"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios', verbose_name="Publicación")
    nombre_comentarista = models.CharField(max_length=100, verbose_name="Nombre del Comentarista")
    email_comentarista = models.EmailField(verbose_name="Email del Comentarista")
    contenido = models.TextField(max_length=1000, verbose_name="Comentario")
    fecha_comentario = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Comentario")
    aprobado = models.BooleanField(default=True, verbose_name="Aprobado")
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-fecha_comentario']
        
    def __str__(self):
        return f"Comentario de {self.nombre_comentarista} en {self.post.titulo}"