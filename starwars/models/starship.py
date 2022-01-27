from django.db import models

from .person import Person
from .transport import Transport


class Starship(Transport):
    """A starship is a transport with a hypderdrive"""

    hyperdrive_rating = models.CharField(max_length=40)
    MGLT = models.CharField(max_length=40)
    starship_class = models.CharField(max_length=40)
    pilots = models.ManyToManyField(Person, related_name="starships", blank=True)

    def __str__(self):
        return self.starship_class
