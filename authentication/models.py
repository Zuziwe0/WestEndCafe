from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
USER_TYPES = (
    ('Admin', 'Admin'),
    ('Customer', 'Customer'),
)
class CustomeUser(AbstractUser):

    user_type = models.CharField(choices=USER_TYPES, max_length=9, default='Customer')
    
    def __str__(self):
        return f"{self.username} - {self.user_type}"