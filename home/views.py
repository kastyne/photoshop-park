from database.models import course, blog, artwork
from django.shortcuts import render


def homepage(request):
    return render(request, 'home/homepage.html', { # passes varibles to template file
        'courses': course.Course.objects.all()[:3], # First 3 most popular courses
        'categories': blog.Category.objects.all(),
        'art_list': artwork.Artwork.objects.all(),
        'articles': blog.Article.objects.all()[:6],
    })


def about(request):
    return render(request, 'home/about.html')
