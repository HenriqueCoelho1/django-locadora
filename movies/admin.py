from django.contrib import admin
from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "stock")

    # def get_genres(self, obj):
    #     return ", ".join([m.name for m in obj.genres.all()])


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
