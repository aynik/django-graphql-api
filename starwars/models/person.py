from django.db import models

from .base_models import DateTimeModel
from .planet import Planet


class Person(DateTimeModel):
    """A person i.e. - Luke Skywalker"""

    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True)
    mass = models.CharField(max_length=10, blank=True)
    hair_color = models.CharField(max_length=20, blank=True)
    skin_color = models.CharField(max_length=20, blank=True)
    eye_color = models.CharField(max_length=20, blank=True)
    birth_year = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=40, blank=True)
    homeworld = models.ForeignKey(
        Planet, related_name="residents", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
