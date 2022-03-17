from django.contrib import admin
from database.models import course, blog, user


@admin.register(course.Course, course.Lesson)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors')
    list_filter = ('authors',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(blog.Article)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors')
    list_filter = ('authors', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(blog.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(user.PsUser)
class PsUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
