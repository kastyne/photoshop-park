import imp
from django.urls import path
from .views import ArtworkList, ArtworkDetails

urlpatterns = [
    path('', ArtworkList.as_view(), name="artwork_list"),
    path('<slug:username>/<slug:artwork>', ArtworkDetails.as_view(), name="artwork_details")
]