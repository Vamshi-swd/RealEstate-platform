# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import RegexValidator

class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('agent', 'Agent'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    
    phone_number = PhoneNumberField(
        verbose_name='Phone Number',
        blank=True,
        null=True,
        unique=True,
        help_text='Enter a valid phone number in E.164 format.'
    )
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_expiration = models.DateTimeField(blank=True, null=True)
    otp_verified = models.BooleanField(default=False)
    
    # Define unique related_name attributes to avoid clashes
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return self.username

    def is_otp_expired(self):
        if self.otp_expiration and self.otp_expiration < timezone.now():
            return True
        return False