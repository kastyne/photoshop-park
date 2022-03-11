from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='course-list'),
    path('courses/<slug:slug>/', views.CourseDetails.as_view(), name='course-details')
]
