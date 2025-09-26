from django.urls import path
from . import views

app_name = 'blog' 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('crear-comentario/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar_posts, name='buscar_posts'),
]