from operator import mod
from database.models.user import PsUser as User
from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=120)
    authors = models.ForeignKey(User, on_delete=models.CASCADE, related_name="artwork")
    slug = models.CharField(max_length=120, default="")
    likes = models.IntegerField()
    image = models.URLField()

    class Meta:
        ordering = ['likes']
