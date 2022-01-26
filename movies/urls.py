from unicodedata import name
from django.urls import path

from .views import CreateMovie, CreateGenre


urlpatterns = [
    path("movies/register/", CreateMovie.as_view(), name="create_movie"),
    path("genres/register/", CreateGenre.as_view(), name="create_genre"),
]
