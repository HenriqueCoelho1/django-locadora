from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Movie, Genre


class CreateMovie(CreateView):
    model = Movie
    fields = ["name", "description", "price", "stock", "image", "genre"]
    template_name = "register/form.html"
    success_url = reverse_lazy("index")


class CreateGenre(CreateView):
    model = Genre
    fields = ["name", "description"]
    template_name = "register/form.html"
    success_url = reverse_lazy("index")


# UPDATE
class UpdateMovie(UpdateView):
    model = Movie
    fields = ["name", "description", "price", "stock", "genre"]
    template_name = "register/form.html"
    success_url = reverse_lazy("index")


class UpdateGenre(UpdateView):
    model = Movie
    fields = ["name", "description"]
    template_name = "register/form.html"
    success_url = reverse_lazy("index")


# DELETE


class DeleteGenre(DeleteView):
    model = Genre
    template_name = "register/form-delete.html"
    success_url = reverse_lazy("index")


class DeleteMovie(DeleteView):
    model = Movie
    template_name = "register/form-delete.html"
    success_url = reverse_lazy("index")


# LIST


class ListGenre(ListView):
    model = Genre
    template_name = "genres.html"


class ListMovie(ListView):
    model = Movie
    template_name = "movies.html"
