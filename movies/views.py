from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Movie, Genre


class CreateMovie(CreateView):
    model = Movie
    fields = ["name", "description", "price", "stock", "genre"]
    template_name = "register/form.html"
    success_url = reverse_lazy("index")


class CreateGenre(CreateView):
    model = Genre
    fields = ["name", "description"]
    template_name = "register/form.html"
    success_url = reverse_lazy("index")


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
