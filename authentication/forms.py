from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomeUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomeUser
        fields = ['username','email', 'password1', 'password2']

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if CustomeUser.objects.filter(email=email).exists():
                raise ValidationError('An account with this email already exists.')
            return email

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
