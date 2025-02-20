# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    return login(request, template_name='users/login.html', redirect_field_name='next')

def user_logout(request):
    return logout(request, next_page='home')

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', {'user': request.user})
    else:
        return redirect('login')