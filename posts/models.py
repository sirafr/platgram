"""POST MODELS"""

# Django
from django.db import models

class User(models.Model):
    """User model"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # Usuario administrador
    is_admin = models.BooleanField(default=False)

    bio = models.TextField()

    birthdate = models.DateField(blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Reto

    country = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)

    def __str__(self):
        """Return email"""
        return self.email