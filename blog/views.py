from django.http import HttpResponse
from django.template import loader
from database.models.blog import Article


def index(request):
    article_list = Article.objects.all().filter(status=1)

    template = loader.get_template('blog/index.html')

    context = {
        'article_list': article_list,
    }
    return HttpResponse(template.render(context, request))

def drafts(request):
    article_list = Article.objects.all().filter(status=0)

    template = loader.get_template('blog/index.html')

    context = {
        'article_list': article_list,
    }
    return HttpResponse(template.render(context, request))