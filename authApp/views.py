from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput, PasswordInput
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import UserLoginForm
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'authApp/login.html', {'form': form})

def logout(request):
    print('hello')
#     auth_logout(request)
#     return redirect('home')
#
def register(request):
    print('hello')

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_superuser = False
#             password = form.cleaned_data['password1']
#             user.set_password(password)
#             user.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'authApp/register.html', {'form': form})
