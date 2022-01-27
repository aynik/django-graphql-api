from django.db import models

from .person import Person
from .transport import Transport


class Vehicle(Transport):
    """A vehicle is anything without hyperdrive capability"""

    vehicle_class = models.CharField(max_length=40)
    pilots = models.ManyToManyField(Person, related_name="vehicles", blank=True)

    def __str__(self):
        return self.vehicle_class
