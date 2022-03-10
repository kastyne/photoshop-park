from statistics import mode
from tkinter import CASCADE
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length="50")
    discription = models.CharField(max_length="120")
    image = models.URLField()

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=CASCADE)

    name = models.CharField(max_length="50")
    discription = models.CharField(max_length="120")