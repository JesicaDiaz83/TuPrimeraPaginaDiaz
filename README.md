# TuPrimeraPaginaDiaz - Entrega Final Django

## Descripción
Proyecto final del curso de Python con Django. Blog avanzado con sistema de usuarios, páginas con CKEditor, mensajería y gestión de imágenes.

## Características Principales
- Sistema de usuarios (registro, login, perfiles)
- App Pages con CKEditor para contenido enriquecido  
- App Messenger para comunicación entre usuarios
- Manejo de imágenes (avatares, imágenes de páginas)
- CBV con mixins personalizados
- Vista función con decorador @login_required
- Herencia de templates
- Panel de administración completo
- Blog original mantenido

## Tecnologías
- Python 3.8+
- Django 4.2.7
- django-ckeditor
- Pillow (manejo de imágenes)
- Bootstrap 5

## URLs Principales
- `/` - Lista de páginas (página principal)
- `/about/` - Acerca de (requiere login) 
- `/accounts/signup/` - Registro
- `/accounts/login/` - Login
- `/accounts/profile/` - Perfil usuario
- `/messenger/send/` - Enviar mensaje
- `/messenger/inbox/` - Ver mensajes recibidos
- `/blog/` - Blog original (mantenido)
- `/admin/` - Panel administración

## Video Demostrativo

Puedes ver la demostración completa del proyecto en:
- **Google Drive:** [\[Link al video\]](https://drive.google.com/file/d/1R4binSiewF_MINHALvXymIgfDX3ZQY_A/view?usp=sharing)

Duración: 8 minutos

## Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/JesicaDiaz83/TuPrimeraPaginaDiaz.git
cd TuPrimeraPaginaDiaz