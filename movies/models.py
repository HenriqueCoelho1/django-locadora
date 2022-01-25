from tkinter import CASCADE
from django.db import models


class Genre(models.Model):
    name = models.CharField("Name", max_length=200)
    description = models.TextField("Description")

    def __str__(self):
        return f"{self.name}, {self.description}"


class Movie(models.Model):
    name = models.CharField("Name", max_length=200)
    description = models.TextField("Description")
    price = models.DecimalField(decimal_places=1, max_digits=4)
    stock = models.IntegerField("Stock")

    # gender = models.ForeignKey(Genres, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.genre}"
