from django.template.defaultfilters import slugify
from database.models.user import PsUser as User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=120)
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=240)
    slug = models.CharField(max_length=120, default="")
    image = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Lesson(models.Model):
    course = models.ManyToManyField(Course, related_name="lessons")
    title = models.CharField(max_length=120, default="")
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=240)
    created_on = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=120, default="")
    image = models.URLField(blank=True)
    content = models.TextField(default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)
