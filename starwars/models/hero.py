from django.db import models

from .base_models import DateTimeModel
from .planet import Planet


class Hero(DateTimeModel):
    name = models.CharField(max_length=100)
    homeworld = models.ForeignKey(
        Planet, related_name="heroes", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
