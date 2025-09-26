from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=300, blank=True, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")  # CKEditor
    image = models.ImageField(upload_to='pages/', blank=True, null=True, verbose_name="Imagen")
    created_date = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('pages:detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)