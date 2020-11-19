from django.db import models

from .base_models import DateTimeModel
from .person import Person
from .planet import Planet


class Species(DateTimeModel):
    "A species is a type of alien or person"

    name = models.CharField(max_length=40)
    classification = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    average_height = models.CharField(max_length=40)
    skin_colors = models.CharField(max_length=200)
    hair_colors = models.CharField(max_length=200)
    eye_colors = models.CharField(max_length=200)
    average_lifespan = models.CharField(max_length=40)
    homeworld = models.ForeignKey(
        Planet, blank=True, null=True, on_delete=models.CASCADE
    )
    language = models.CharField(max_length=40)
    people = models.ManyToManyField(Person, related_name="species")

    def __str__(self):
        return self.name
