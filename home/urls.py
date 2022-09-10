from django.urls import path, include
from home.views import homepage, about

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
]
