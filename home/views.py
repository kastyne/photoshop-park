from database.models import course, blog, artwork
from django.shortcuts import render


def homepage(request):
    courses = course.CourseListView.objects.all()
    categories = blog.Category.objects.all()
    art_list = artwork.Artwork.objects.all()
    articles = blog.Article.objects.all()

    return render(request, 'home/homepage.html', {
        'courses': courses,
        'categories': categories,
        'art_list': art_list,
        'articles': articles
    })


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')
