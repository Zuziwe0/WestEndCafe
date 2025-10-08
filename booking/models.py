from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1)
    special_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
