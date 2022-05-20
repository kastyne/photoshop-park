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

    def __init__(self, *args, **kwargs):
        super(LessonAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['courses'].initial = self.instance.courses.all()

@admin.register(course.Lesson)
class LessonAdmin(admin.ModelAdmin):
   form = LessonAdminForm

   def save_model(self, request, obj, form, change):
       original_lessons = obj.courses.all()
       new_lessons = form.cleaned_data['lessons']
       remove_qs = original_lessons.exclude(id__in=new_lessons.values('id'))
       add_qs = new_lessons.exclude(id__in=original_lessons.values('id'))


       obj.save()   

       for item in remove_qs:
               obj.courses.remove(item)
       for item in add_qs:
               obj.courses.add(item)

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