from database.models.course import Course, Lesson
from django.views import generic

class CourseList(generic.ListView):
    model = Course
    template_name = 'home/index.html'

class CourseDetails(generic.DetailView):
    model = Course
    template_name = 'home/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = context['object'].lessons.all()
        
        return context