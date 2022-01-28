from django.db import models

from .base_models import DateTimeModel


class Planet(DateTimeModel):
    """A planet i.e. Tatooine"""

    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=40)
    orbital_period = models.CharField(max_length=40)
    diameter = models.CharField(max_length=40)
    climate = models.CharField(max_length=40)
    gravity = models.CharField(max_length=40)
    terrain = models.CharField(max_length=40)
    surface_water = models.CharField(max_length=40)
    population = models.CharField(max_length=40)

    def __str__(self):
        return self.name
