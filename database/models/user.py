from django.contrib.auth.models import AbstractUser
from django.db import models


class PsUser(AbstractUser):
    username = models.CharField(max_length=64, default='', unique=True)
    avatar = models.URLField(blank=True, default='https://i.scdn.co/image/ab6761610000e5ebfd30ebd7e80dad6b2383aab0')
    email = models.EmailField(max_length=64, unique=True)
    enrollment = models.ManyToManyField('Course', through='Enrollment')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
