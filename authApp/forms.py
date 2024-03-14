from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(ModelForm):
    class Meta:
        # model = UserProfile
        fields = ['username', 'email', 'password']

        widgets = {
            "username": TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            "email": EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}),
            "password": PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={'class': 'form-login'}),
            "password": PasswordInput(attrs={'class': 'form-login'})
        }