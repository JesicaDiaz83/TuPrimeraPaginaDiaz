from django import forms
from .models import Autor, Post, Comentario

class AutorForm(forms.ModelForm):
    """Formulario para crear/editar autores"""
    
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'email', 'biografia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'biografia': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Breve biografía del autor...'
            }),
        }

class PostForm(forms.ModelForm):
    """Formulario para crear/editar publicaciones"""
    
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'publicado']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la publicación'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Escriba el contenido de la publicación...'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'publicado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class ComentarioForm(forms.ModelForm):
    """Formulario para crear comentarios"""
    
    class Meta:
        model = Comentario
        fields = ['post', 'nombre_comentarista', 'email_comentarista', 'contenido']
        widgets = {
            'post': forms.Select(attrs={
                'class': 'form-control'
            }),
            'nombre_comentarista': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Su nombre'
            }),
            'email_comentarista': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'su@email.com'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escriba su comentario...'
            }),
        }

class BusquedaForm(forms.Form):
    """Formulario para buscar publicaciones"""
    busqueda = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar publicaciones...',
            'type': 'search'
        }),
        label='Búsqueda'
    )