from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_option', 'proof']
        widgets = {
            'payment_option': forms.Select(attrs={'class': 'form-control'}),
            'proof': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }