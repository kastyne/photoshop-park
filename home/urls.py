from django.urls import path, include
from home.views import homepage, about, contact

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
