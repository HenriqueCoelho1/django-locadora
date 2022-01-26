from unicodedata import name
from django.urls import path, include
from .views import IndexView, TestView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("testing/", TestView.as_view(), name="testing"),
    path("", include("movies.urls"), name="movies"),
]
