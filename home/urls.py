from django.urls import path, include
from home.views import homepage, about, contact

urlpatterns = [
    path('', homepage),
    path('about/', about),
    path('contact/', contact)
]
