from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='course-list'),
    path('<str:name>/', views.CourseDetails.as_view(), name='course-details')
]
