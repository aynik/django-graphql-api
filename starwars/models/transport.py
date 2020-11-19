from django.db import models

from .base_models import DateTimeModel


class Transport(DateTimeModel):
    name = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    manufacturer = models.CharField(max_length=80)
    cost_in_credits = models.CharField(max_length=40)
    length = models.CharField(max_length=40)
    max_atmosphering_speed = models.CharField(max_length=40)
    crew = models.CharField(max_length=40)
    passengers = models.CharField(max_length=40)
    cargo_capacity = models.CharField(max_length=40)
    consumables = models.CharField(max_length=40)

    def __str__(self):
        return self.name
