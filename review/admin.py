from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'rating', 'date_created')
    list_filter = ('rating', 'date_created')
    search_fields = ('user__username', 'item__name', 'comment')
    ordering = ('-date_created',)
    readonly_fields = ('date_created',)
    list_editable = ('rating',)
    raw_id_fields = ('user', 'item')