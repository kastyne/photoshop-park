from django.urls import path, include
from pages.views import home

urlpatterns = [
    path('', home.index)
]
