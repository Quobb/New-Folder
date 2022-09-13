from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('newApp/', include('newApp.urls')),
    path('admin/', admin.site.urls),
]