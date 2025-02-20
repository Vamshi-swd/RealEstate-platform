# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
     path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),

   
]