# users/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import RegisterForm
from .utils import send_otp
import random

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')  # Replace 'home' with the name of the view where you want to redirect after login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            otp = str(random.randint(100000, 999999))
            otp_expiration = timezone.now() + timezone.timedelta(minutes=10)  # OTP expires in 10 minutes
            request.session['otp'] = otp  # Store OTP in session
            request.session['phone_number'] = str(phone_number)  # Store phone number in session
            request.session['otp_expiration'] = otp_expiration.timestamp()  # Store OTP expiration in session
            send_otp(phone_number, otp)  # Send OTP to the user's phone number
            return redirect('verify_otp')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        if user_otp == stored_otp:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                authenticate(request, user)
                return redirect('home')
        else:
            return render(request, 'users/verify_otp.html', {'error': 'Invalid OTP'})
    return render(request, 'users/verify_otp.html')

def home(request):
    return render(request, 'home.html')

def terms(request):
    return render(request, 'users/terms.html')

def user_logout(request):
    return logout(request, next_page=reverse_lazy('login'))

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', {'user': request.user})
    else:
        return redirect('login')
    
def privacy(request):
    return render(request, 'users/privacy.html')