from django.urls import path, include
from users.views import register

urlpatterns = [
    path('', register),
]
