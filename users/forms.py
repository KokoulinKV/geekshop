from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter password'}))

    class Meta:
        model = User
        fields = ('password', 'username')