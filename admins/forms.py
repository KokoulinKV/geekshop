from django import forms
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