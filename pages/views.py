from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Page
from .forms import PageForm

# Mixin personalizado para verificar propiedad
class OwnerRequiredMixin:
    """Mixin que permite solo al propietario editar/eliminar"""
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            messages.error(self.request, 'No tienes permisos para realizar esta acción.')
            return redirect('pages:list')
        return obj

# CBV 1: ListView para mostrar todas las páginas
class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'
    paginate_by = 5
    
    def get_queryset(self):
        return Page.objects.all()

# CBV 2: DetailView para mostrar página individual
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    context_object_name = 'page'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

# CBV 3: CreateView con LoginRequiredMixin
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/create.html'
    success_url = reverse_lazy('pages:list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, '¡Página creada exitosamente!')
        return super().form_valid(form)

# CBV 4: UpdateView con OwnerRequiredMixin
class PageUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/edit.html'
    success_url = reverse_lazy('pages:list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada exitosamente!')
        return super().form_valid(form)

# CBV 5: DeleteView con OwnerRequiredMixin
class PageDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('pages:list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Página eliminada exitosamente!')
        return super().delete(request, *args, **kwargs)

# Vista función con decorador @login_required
@login_required
def about_view(request):
    """Vista 'Acerca de mí' - requiere estar logueado"""
    return render(request, 'pages/about.html', {
        'title': 'Acerca de mí',
        'user': request.user,
        'profile': request.user.profile
    })
