from database.models import course, blog, user, artwork

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib import admin

from django import forms

@admin.register(course.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors')
    list_filter = ('authors',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class LessonAdminForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset = course.Course.objects.all(),
        widget = FilteredSelectMultiple(verbose_name='lessons', is_stacked=False))

    class Meta:
        model = course.Lesson
        fields = ['title', 'authors', 'description', 'image', 'content']

@admin.register(course.Lesson)
class LessonAdmin(admin.ModelAdmin):
   form = LessonAdminForm

   def save_model(self, request, obj, form, change):
       super().save_model(request, obj, form, change)

       original_lessons = set(obj.courses.values_list("id", flat=True))
       current_lessons = set(map(lambda x: x.id, form.cleaned_data['courses']))

       if original_lessons != current_lessons:
           add_to_course = current_lessons - original_lessons
           for course_to_change in course.Course.objects.filter(id__in=add_to_course):
                course_to_change.lessons.add(obj)
           
           remove_from_course = original_lessons - current_lessons
           for course_to_change in course.Course.objects.filter(id__in=remove_from_course):
               course_to_change.lessons.remove(obj)


@admin.register(blog.Article)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors')
    list_filter = ('authors', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(blog.Category, artwork.Artwork)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(user.PsUser)
class PsUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')

admin.site.register(course.Enrollment)