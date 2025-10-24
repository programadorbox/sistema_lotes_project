from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)

    ROL_CHOICES = [
        ('vendedor', 'Vendedor'),
        ('supervisor', 'Supervisor'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='vendedor')

    def __str__(self):
        return f"{self.username} ({self.rol})"
