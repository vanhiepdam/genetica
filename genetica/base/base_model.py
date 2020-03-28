# -*- coding: utf-8 -*-
from uuid import uuid4

from django.db import models


class ModelBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text='Created at')

    updated_at = models.DateTimeField(auto_now=True,
                                      null=True,
                                      help_text='Updated at')

    class Meta:
        abstract = True
