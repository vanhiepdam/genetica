from django.db import models

from genetica.base.base_model import ModelBase


class Service(ModelBase):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.1)

    def __str__(self):
        return self.name
