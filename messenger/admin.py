from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'subject')
    ordering = ('-created_at',)
