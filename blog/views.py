from django.views import generic
from database.models.blog import Article


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1)
    context_object_name = 'article_list'
    template_name = 'blog/index.html'


class DraftList(generic.ListView):
    queryset = Article.objects.filter(status=0)
    template_name = 'blog/index.html'


class ArticleDetails(generic.DetailView):
    model = Article
    template_name = 'blog/article_details.html'
