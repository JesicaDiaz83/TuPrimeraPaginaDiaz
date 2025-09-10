from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Autor, Post, Comentario
from .forms import AutorForm, PostForm, ComentarioForm, BusquedaForm

def inicio(request):
    """Vista principal del blog - muestra las últimas publicaciones"""
    posts = Post.objects.filter(publicado=True)[:5]  # Últimas 5 publicaciones
    return render(request, 'blog/inicio.html', {'posts': posts})

def crear_autor(request):
    """Vista para crear un nuevo autor"""
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Autor creado exitosamente!')
            return redirect('inicio')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = AutorForm()
    
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_post(request):
    """Vista para crear una nueva publicación"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Publicación creada exitosamente!')
            return redirect('inicio')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = PostForm()
    
    return render(request, 'blog/crear_post.html', {'form': form})

def crear_comentario(request):
    """Vista para crear un nuevo comentario"""
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Comentario agregado exitosamente!')
            return redirect('inicio')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ComentarioForm()
    
    return render(request, 'blog/crear_comentario.html', {'form': form})

def buscar_posts(request):
    """Vista para buscar publicaciones"""
    form = BusquedaForm()
    posts = []
    busqueda_realizada = False
    
    if request.method == 'GET' and 'busqueda' in request.GET:
        form = BusquedaForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['busqueda']
            posts = Post.objects.filter(
                Q(titulo__icontains=query) | Q(contenido__icontains=query),
                publicado=True
            )
            busqueda_realizada = True
            
            if not posts:
                messages.info(request, f'No se encontraron publicaciones para "{query}"')
            else:
                messages.success(request, f'Se encontraron {posts.count()} publicaciones para "{query}"')
    
    context = {
        'form': form,
        'posts': posts,
        'busqueda_realizada': busqueda_realizada
    }
    return render(request, 'blog/buscar_posts.html', context)