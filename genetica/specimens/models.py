from django.db import models

from genetica.base.base_model import ModelBase
from genetica.services.models import Service
from genetica.user_profiles.models import UserProfile


class TestStep(ModelBase):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """To string.
        """
        return self.name


class Specimen(ModelBase):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(choices=[
        ('prepare', 'Prepare'),
        ('processing', 'Processing'),
        ('done', 'Done')
    ], max_length=20, default='prepare')
    user_profile = models.ForeignKey(
        UserProfile,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='specimens'
    )
    service = models.ForeignKey(
        Service,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='specimens'
    )
    steps = models.ManyToManyField(
        TestStep,
        blank=True,
    )

    def __str__(self):
        """To string.
        """
        return self.name
