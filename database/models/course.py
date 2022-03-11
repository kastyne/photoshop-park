from turtle import update
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    image = models.URLField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    created_on = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.name
