from django.urls import path

from .views import (
    CreateMovie,
    CreateGenre,
    UpdateGenre,
    UpdateMovie,
    DeleteGenre,
    DeleteMovie,
    ListGenre,
    ListMovie,
)


urlpatterns = [
    path("movies/register/", CreateMovie.as_view(), name="create_movie"),
    path("genres/register/", CreateGenre.as_view(), name="create_genre"),
    path("movies/update/<int:pk>/", UpdateMovie.as_view(), name="update_movie"),
    path("genres/update/<int:pk>/", UpdateGenre.as_view(), name="update_genre"),
    path("movies/delete/<int:pk>/", DeleteMovie.as_view(), name="delete_movie"),
    path("genres/delete/<int:pk>/", DeleteGenre.as_view(), name="delete_genre"),
    path("genres/", ListGenre.as_view(), name="list_genre"),
    path("movies/", ListMovie.as_view(), name="list_movie"),
]
