from django.contrib import admin
from database.models import course, blog

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors')
    list_filter = ('authors', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(course.Course, CourseAdmin)
admin.site.register(course.Lesson, CourseAdmin)
admin.site.register(blog.Article)