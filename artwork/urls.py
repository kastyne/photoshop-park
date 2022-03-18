import imp
from django.urls import path
from views import ArtworkList

urlpatterns = [
    path('', ArtworkList.as_view(), name="artwork_list")
]