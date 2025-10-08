from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('Orders', 'Orders'),
        ('Bookings', 'Bookings'),
        ('Reviews', 'Reviews'),
    ]
    
    name = models.CharField(max_length=100)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    generated_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_count = models.PositiveIntegerField(default=0)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    file = models.FileField(upload_to='reports/', null=True, blank=True)

    def __str__(self):
        return f"{self.report_type} report ({self.start_date} to {self.end_date})"

    class Meta:
        ordering = ['-generated_at']
    verbose_name = 'Report'
    verbose_name_plural = 'Reports'