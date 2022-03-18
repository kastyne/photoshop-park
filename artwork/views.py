from database.models.artwork import Artwork
from django.views import generic


class ArtworkList(generic.ListView):
    model = Artwork
    template_name = 'artwork/index.html'