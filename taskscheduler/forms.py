from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from .models import AppPassword
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]

class PasswordForm(forms.ModelForm):

    class Meta:
        model = AppPassword 
        fields = ["app_password"]