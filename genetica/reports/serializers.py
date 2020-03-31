# -*- coding: utf-8 -*-
from django.db.models import QuerySet
from rest_framework import serializers

from genetica.reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    meta = serializers.JSONField()
    state = serializers.CharField()
    service_name = serializers.CharField(source='service.name')
    profile_name = serializers.CharField(source='user_profile.name')
    user_email = serializers.CharField(source='user_profile.account.email')

    @classmethod
    def setup_eager_loading(cls, queryset: QuerySet):
        return queryset.select_related('service', 'user_profile', 'user_profile__account')

    class Meta:
        """Meta class.
        """
        model = Report
        fields = (
            'id',
            'name',
            'description',
            'meta',
            'state',
            'service_name',
            'profile_name',
            'user_email',
        )
