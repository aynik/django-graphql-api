from django.db import models

from .base_models import DateTimeModel
from .person import Person
from .planet import Planet
from .species import Species
from .starship import Starship
from .vehicle import Vehicle


class Film(DateTimeModel):
    """A film i.e. The Empire Strikes Back (which is also the best film)"""

    title = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField()
    characters = models.ManyToManyField(Person, related_name="films", blank=True)
    planets = models.ManyToManyField(Planet, related_name="films", blank=True)
    starships = models.ManyToManyField(Starship, related_name="films", blank=True)
    vehicles = models.ManyToManyField(Vehicle, related_name="films", blank=True)
    species = models.ManyToManyField(Species, related_name="films", blank=True)

    def __str__(self):
        return self.title
