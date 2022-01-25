from unicodedata import name
from django.urls import path
from .views import IndexView, TestView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("testing/", TestView.as_view(), name="testing"),
    # path("/movies", MoviesView.as_view(), name="movies"),
]
