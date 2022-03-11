from operator import mod
from telnetlib import STATUS
from turtle import title
from django.contrib.syndication.views import Feed
from django.contrib.auth.models import User
from django.db import models

class BlogFeed(Feed):
    title = "Phototshop Park"
    link = "/blog/"

    author_email = "kait@photoshoppark" # change later

    def item_author_name(self, item):
        return item.author

    def items(self):
        return Article.objects.filter(status= 1)

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class Article(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0)
    
    slug = models.SlugField(max_length=240, unique=True)
    created_on = models.DateField(auto_now_add=True)
    
    description = models.CharField(max_length=240)
    content = models.TextField()

    class Meta:
        ordering = ['_created-on']

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog.views.article', (), {
            'year': self.created_on.year,
            'month': self.created_on.strftime('%m'),
            'slug': self.slug})
