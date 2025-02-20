# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('agent', 'Agent'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    # Define unique related_name attributes to avoid clashes
    groups = models.ManyToManyField('auth.Group', related_name='%(app_label)s_%(class)s_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='%(app_label)s_%(class)s_user_permissions', blank=True)