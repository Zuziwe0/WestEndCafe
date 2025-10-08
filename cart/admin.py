from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'item__name')
    ordering = ('-added_at',)
    readonly_fields = ('added_at',)
    list_editable = ('quantity',)
    raw_id_fields = ('user', 'item')