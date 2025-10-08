from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['item', 'rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'item': 'Menu Item',
            'rating': 'Rating (1-5)',
            'comment': 'Your Review',
        }