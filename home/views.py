from re import template
from unicodedata import category
from database.models import course, blog, artwork
from django.shortcuts import render

def homepage(request):
    course_list = course.Course.objects.all()
    categories = blog.Category.objects.all()
    art_list = artwork.Artwork.objects.all()

    return render(request, 'home/homepage.html', {
        'course_list': course_list,
        'categories': categories,
        'art_list': art_list
    })

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')