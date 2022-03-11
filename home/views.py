from re import template
from database.models import course, blog
from django.shortcuts import render

def homepage(request):
    course_list = course.Course.objects.all()
    article_list = blog.Article.objects.filter(status=1)

    return render(request, 'home/homepage.html', {
        'course_list': course_list,
        'article_list': article_list,
    })

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')