from django.contrib.auth.models import AbstractUser
from django.db import models


class PsUser(AbstractUser):
    username = models.CharField(max_length=64, default='', unique=True)
    email = models.EmailField(max_length=64, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username