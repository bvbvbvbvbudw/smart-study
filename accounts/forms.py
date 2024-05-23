from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, UserRole

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=UserRole.ROLE_CHOICES, required=True, label="Role")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        if commit:
            user.save()
            user_role = UserRole(user=user, role=role)
            if role == 'admin':
                user_role.is_admin = True
            user_role.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
