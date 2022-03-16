from django.template.defaultfilters import slugify
from django.contrib.syndication.views import Feed
from django.contrib.auth.models import User
from django.db import models


class BlogFeed(Feed):
    title = "Photoshop Park"
    link = "/blog/"

    author_email = "kait@photoshoppark"  # change later

    def item_author_name(self, item):
        return item.author

    def items(self):
        return Article.objects.filter(status=1)


STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Article(models.Model):
    title = models.CharField(max_length=120)
    # authors = models.CharField(max_length=50, default="Photoshop Park")
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    # publications = models.ManyToManyField(Publication)

    image = models.URLField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    slug = models.SlugField(max_length=240, unique=True)
    created_on = models.DateField(auto_now_add=True)

    description = models.CharField(max_length=240)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
