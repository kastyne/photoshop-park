from django.urls import path, include
from courses import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='course-list'),
    path('<slug:slug>/', views.CourseDetails.as_view(), name='course-details')
]
