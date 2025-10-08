from django import forms

class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=20, initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    # The 'update' field indicates whether to update the quantity or add to it