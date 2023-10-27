from django.contrib import admin
from chat.models.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'seen', 'date_created')
