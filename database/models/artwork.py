from cloudinary.models import CloudinaryField
from django.db import models
from django.template.defaultfilters import slugify
from database.models.user import PsUser as User


class Artwork(models.Model):
    title = models.CharField(max_length=120)
    authors = models.ForeignKey(User, on_delete=models.CASCADE, related_name="artwork")
    slug = models.CharField(max_length=120, default="")
    likes = models.IntegerField(default=0)
    image = CloudinaryField('image')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Artwork, self).save(*args, **kwargs)

        # get cloudinary (hosting) url and save to url
        if self.url == '':
            self.url = str(f'https://res.cloudinary.com/dhnyjvjec/image/upload/{self.image.public_id}')
            self.save()

    class Meta:
        ordering = ['likes']
