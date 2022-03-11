from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drafts/', views.drafts)
]
