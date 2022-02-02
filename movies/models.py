import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename


class Base(models.Model):
    created = models.DateField("Creation", auto_now_add=True)
    modified = models.DateField("Updated", auto_now=True)
    is_active = models.BooleanField("Active", default=True)

    class Meta:
        abstract = True


class Genre(Base):
    name = models.CharField("Name", max_length=200)
    description = models.TextField("Description")

    def __str__(self):
        return f"{self.name}, {self.description}"


class Movie(Base):
    name = models.CharField("Name", max_length=200)
    description = models.TextField("Description")
    image = StdImageField(
        "Image",
        upload_to=get_file_path,
        variations={"thumb": {"width": 450, "height": 610, "crop": True}},
    )
    price = models.DecimalField(decimal_places=1, max_digits=4)
    stock = models.IntegerField("Stock")

    genre = models.ManyToManyField("Genre", related_name="movies")

    def __str__(self):
        return f"{self.name}, {self.description}"
