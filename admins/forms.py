from django import forms
from django.contrib.auth.forms import UserCreationForm

from products.models import Product, ProductCategory
from users.forms import UserRegistrationFrom, UserProfileForm
from users.models import User


class UserAdminsRegistrationForm(UserRegistrationFrom):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminsProfileForm(UserProfileForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))


class ProductAdminsCreationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter name'}))
    price = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter price'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter description'}), required=False)
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Enter quantity in stock', 'min': 0}))
    category = forms.ModelChoiceField(queryset = ProductCategory.objects.all(), label='ds',
        widget=forms.Select(attrs={'class': 'form-control py-4', 'placeholder': 'Enter category'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)


    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'quantity', 'category', 'image')
