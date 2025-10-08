from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'payment_option', 'status', 'date_created')
    inlines = [OrderItemInline]
    list_filter = ('status', 'payment_option', 'date_created')
    search_fields = ('user__username',)
