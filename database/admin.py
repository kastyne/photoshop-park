from django.contrib import admin

from database.models import course, blog

admin.site.register(course.Course)
admin.site.register(course.Lesson)
admin.site.register(blog.Article)