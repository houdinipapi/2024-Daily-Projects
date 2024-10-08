from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")
    username = forms.CharField(max_length=30, required=True, help_text="Required")
    password1 = forms.CharField(widget=forms.PasswordInput, help_text="Required")
    password2 = forms.CharField(widget=forms.PasswordInput, help_text="Required")


    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, help_text="Required")
    password = forms.CharField(widget=forms.PasswordInput, help_text="Required")

