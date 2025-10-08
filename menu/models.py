from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    def get_price(self):
        return self.price   
    class Meta:
        ordering = ['name'] 
    verbose_name = 'Menu Item'
    verbose_name_plural = 'Menu Items'
    indexes = [
        models.Index(fields=['name']),
        models.Index(fields=['category']),
    ]
    def save(self, *args, **kwargs):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        super().save(*args, **kwargs)
        
    def is_available(self):
        return self.available
    
    def toggle_availability(self):
        self.available = not self.available
        self.save()

    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price
        self.save()
