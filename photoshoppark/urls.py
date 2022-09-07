from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Photoshop Park"
admin.site.site_title = "Photoshop Park"

urlpatterns = [
    path('', include('home.urls')),
    path('', include('users.urls')), # /profile and login live on the top level
    path('courses/', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('art/', include('artwork.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')), # tinymce wysiwyg editor
]
