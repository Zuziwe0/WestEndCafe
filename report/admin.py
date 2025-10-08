from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_type', 'start_date', 'end_date', 'total_count', 'total_value', 'generated_at')
    list_filter = ('report_type', 'start_date', 'end_date', 'generated_at')
    search_fields = ('name', 'report_type')
    ordering = ('-generated_at',)
    readonly_fields = ('generated_at',)