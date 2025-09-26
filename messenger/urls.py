from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('send/', views.send_message_view, name='send'),
    path('inbox/', views.inbox_view, name='inbox'),
]