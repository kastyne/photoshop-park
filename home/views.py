from django.http import HttpResponse
from django.template import loader
from database.models.course import Course


def index(request):
    course_list = Course.objects.all()

    template = loader.get_template('home/index.html')

    context = {
        'course_list': course_list,
    }
    return HttpResponse(template.render(context, request))
