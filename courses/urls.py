from django.urls import path, include
from courses import views

urlpatterns = [
    path('', views.CourseList.as_view()),
    path('<slug:slug>/', views.CourseDetails.as_view(), name='course-details'),
    path('<slug:course>/<slug:lesson>', views.LessonDetails.as_view(), name='lesson-details')
]
