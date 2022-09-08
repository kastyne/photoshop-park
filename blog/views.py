from django.views import generic
from database.models.blog import Article, Category


class ArticleList(generic.ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'blog/index.html'

class DraftList(generic.ListView):
    queryset = Article.objects.filter(status=0)
    template_name = 'blog/index.html'


class ArticleDetails(generic.DetailView):
    model = Article
    template_name = 'blog/article_details.html'

class CategoryList(generic.ListView):
    template_name = 'blog/category_list.html'
    model = Category

class CategoryDetails(generic.TemplateView):
    template_name = 'blog/category_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(title=kwargs['title'])

        context['articles'] = category.articles.all()
        context['category'] = category

        # it most definetly did not take me an hour of debugging to figure out that i forgot the return
        return context
