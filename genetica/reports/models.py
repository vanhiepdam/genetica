from django.contrib.postgres.fields import JSONField
from django.db import models

from genetica.base.base_model import ModelBase
from genetica.services.models import Service
from genetica.user_profiles.models import UserProfile


class TraitTemplate(ModelBase):
    name = models.CharField(max_length=255)
    template = JSONField(blank=True, default={})
    level = models.IntegerField(default=0)

    def __str__(self):
        """To string
        """
        return "{}_{}".format(self.name, self.level)


class Report(ModelBase):
    STATE_PREPARE = 'prepare'
    STATE_READY = 'ready'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    meta = JSONField(blank=True, null=True)
    service = models.ForeignKey(
        Service,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    user_profile = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    state = models.CharField(
        choices=[
            (STATE_PREPARE, 'Preparing'),
            (STATE_READY, 'Ready')
        ],
        max_length=20,
        db_index=True
    )

    def __str__(self):
        """To string
        """
        return self.name


class Trait(ModelBase):
    name = models.CharField(max_length=255)
    data = JSONField(null=True, blank=True)
    template = models.ForeignKey(
        TraitTemplate,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    report = models.ForeignKey(
        Report,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """To string
        """
        return self.name
