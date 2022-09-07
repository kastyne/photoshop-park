from django.views import generic
from database.models.artwork import Artwork
from database.models.user import PsUser


class ArtworkList(generic.ListView):
    model = Artwork
    context_object_name = "artworks"
    template_name = 'artwork/index.html'


class ArtworkDetails(generic.base.TemplateView):
    template_name = 'artwork/art_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = PsUser.objects.get(username=kwargs['username'])

        context['author'] = author
        context['piece'] = author.artwork.get(slug=kwargs['artwork'])

        return context
