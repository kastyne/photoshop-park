from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    slug = models.CharField(max_length=120, default="")
    image = models.URLField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=120, default="")
    authors = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    created_on = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=120, default="")
    image = models.URLField()
    content = models.TextField(default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)
