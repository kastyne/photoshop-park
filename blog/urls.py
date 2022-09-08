from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('drafts/', views.DraftList.as_view(), name='draft_list'),
    path('categories/', views.CategoryList.as_view(), name="category_list"),
    path('categories/<slug:title>/', views.CategoryDetails.as_view(), name='category_details'),
    path('<slug:slug>/', views.ArticleDetails.as_view(), name='article_detail'),
]
