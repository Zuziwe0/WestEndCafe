from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'is_active', 'created_at')
    list_filter = ('is_active', 'date')
    search_fields = ('title', 'description', 'location')
    ordering = ('-date', 'time')