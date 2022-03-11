from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    slug = models.CharField(max_length=120)
    image = models.URLField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs) 


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    created_on = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.name
