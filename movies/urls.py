from unicodedata import name
from django.urls import path

from .views import CreateMovie, CreateGenre, UpdateGenre, UpdateMovie


urlpatterns = [
    path("movies/register/", CreateMovie.as_view(), name="create_movie"),
    path("genres/register/", CreateGenre.as_view(), name="create_genre"),
    path("movies/update/<int:pk>", UpdateMovie.as_view(), name="update_movie"),
    path("genres/update/<int:pk>", UpdateGenre.as_view(), name="update_genre"),
]
