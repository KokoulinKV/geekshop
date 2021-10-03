import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter name'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter password'}))

    class Meta:
        model = User
        fields = ('password', 'username')


class UserRegistrationFrom(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter name'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter email'}))
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter your age', 'min': 0}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter first name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter last name'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter password again'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data):
            raise forms.ValidationError('This email is already taken!')
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data):
            raise forms.ValidationError('This username is already taken!')
        return data

    def save(self, commit=True):
        user = super(UserRegistrationFrom, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'First name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Last name'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter your age', 'min': 0}))

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'first_name', 'last_name', 'image')


class UserProfileEdition(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('tagline', 'gender', 'about_me', 'langs', 'vk_id')

    def __init__(self, *args, **kwargs):
        super(UserProfileEdition, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'gender':
                field.widget.attrs['class'] = 'form-control py-4'
                if field_name == 'vk_id':
                    field.widget.attrs['readonly'] = True
            else:
                field.widget.attrs['class'] = 'form-control'
