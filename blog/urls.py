from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('drafts/', views.DraftList.as_view(), name='draft_list'),
    path('<slug:slug>/', views.ArticleDetails.as_view(), name='article_detail')
]
