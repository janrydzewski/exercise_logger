from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("exercise_logger.urls")),
    path('admin/', admin.site.urls)
]