# users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='free')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Cambia el related_name para evitar el conflicto
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Cambia el related_name para evitar el conflicto
        blank=True
    )

    def is_premium(self):
        return self.role == 'premium'

    def is_free(self):
        return self.role == 'free'
