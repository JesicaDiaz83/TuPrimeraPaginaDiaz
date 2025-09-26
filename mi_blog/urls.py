from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),         # Página principal NUEVA
    path('blog/', include('blog.urls')),     # Tu blog original
    path('accounts/', include('accounts.urls')),   # NUEVA
    path('messenger/', include('messenger.urls')), # NUEVA
    path('ckeditor/', include('ckeditor_uploader.urls')),  # NUEVA
]

# Servir archivos de media en desarrollo (NUEVO)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
