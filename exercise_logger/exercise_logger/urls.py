from django.urls import path
from exercise_logger import views

urlpatterns = [
    path("", views.home, name="home"),
]