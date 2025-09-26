from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.PageListView.as_view(), name='list'),
    path('about/', views.about_view, name='about'),
    path('create/', views.PageCreateView.as_view(), name='create'),
    path('pages/<slug:slug>/', views.PageDetailView.as_view(), name='detail'),
    path('pages/<slug:slug>/edit/', views.PageUpdateView.as_view(), name='edit'),
    path('pages/<slug:slug>/delete/', views.PageDeleteView.as_view(), name='delete'),
]