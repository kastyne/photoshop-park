from database.models.course import Course
from django.views import generic

class CourseList(generic.ListView):
    model = Course
    template_name = 'home/index.html'

class CourseDetails(generic.DetailView):
    model = Course
    template_name = 'home/details.html'