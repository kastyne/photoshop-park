from django.urls import path, include
from essential.views import home

urlpatterns = [
    path('', home.index)
]
