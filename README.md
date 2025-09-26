# TuPrimeraPaginaDiaz - Entrega Final Django

## Descripción
Proyecto final del curso de Python con Django. Blog avanzado con sistema de usuarios, páginas con CKEditor, mensajería y gestión de imágenes.

## Características Principales
- ✅ Sistema de usuarios (registro, login, perfiles)
- ✅ App Pages con CKEditor para contenido enriquecido  
- ✅ App Messenger para comunicación entre usuarios
- ✅ Manejo de imágenes (avatares, imágenes de páginas)
- ✅ CBV con mixins personalizados
- ✅ Vista función con decorador @login_required
- ✅ Herencia de templates
- ✅ Panel de administración completo
- ✅ Blog original mantenido

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

## Funcionalidades por Requisito

### CBV Implementadas
1. `PageListView` - ListView para mostrar páginas
2. `PageDetailView` - DetailView para página individual  
3. `PageCreateView` - CreateView con LoginRequiredMixin
4. `PageUpdateView` - UpdateView con OwnerRequiredMixin
5. `PageDeleteView` - DeleteView con OwnerRequiredMixin

### Mixin Personalizado
- `OwnerRequiredMixin` - Verifica que solo el propietario puede editar/eliminar

### Vista con Decorador
- `about_view` - Vista función con @login_required

### Modelos Principales  
- `Page` - 2 CharField, 1 RichTextField, 1 ImageField, 1 DateField
- `Profile` - Perfil extendido de usuario
- `Message` - Sistema de mensajería

## Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/JesicaDiaz83/TuPrimeraPaginaDiaz.git
cd TuPrimeraPaginaDiaz