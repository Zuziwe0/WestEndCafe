from django.db import models
from django.contrib.auth.models import User
from menu.models import MenuItem 
from django.conf import settings

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} x {self.quantity}"

    def get_total_price(self):
        return self.item.price * self.quantity
