from django.db import models

from genetica.auth.models import User
from genetica.base.base_model import ModelBase
from genetica.services.models import Service


class UserProfile(ModelBase):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    account = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='profiles'
    )
    services = models.ManyToManyField(
        Service,
        blank=True,
    )

    def __str__(self):
        """to string"""
        return self.name
