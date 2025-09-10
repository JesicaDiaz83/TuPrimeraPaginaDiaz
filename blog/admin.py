from django.contrib import admin
from .models import Autor, Post, Comentario

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'fecha_registro')
    list_filter = ('fecha_registro',)
    search_fields = ('nombre', 'apellido', 'email')
    ordering = ('-fecha_registro',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'publicado')
    list_filter = ('publicado', 'fecha_creacion', 'autor')
    search_fields = ('titulo', 'contenido')
    ordering = ('-fecha_creacion',)
    list_editable = ('publicado',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_comentarista', 'post', 'fecha_comentario', 'aprobado')
    list_filter = ('aprobado', 'fecha_comentario')
    search_fields = ('nombre_comentarista', 'contenido')
    ordering = ('-fecha_comentario',)
    list_editable = ('aprobado',)