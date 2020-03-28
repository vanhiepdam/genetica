# -*- coding: utf-8 -*-
from genetica.auth.models import User
from genetica.base.base_service import ServiceBase
from genetica.reports.models import Report


class ReportService(ServiceBase):
    model = Report

    @classmethod
    def list_all_reports(cls):
        return cls.model.objects.all()

    @classmethod
    def list_reports_by_state(cls, state: str):
        return cls.model.objects.filter(state=state)

    @classmethod
    def list_all_reports_by_user(cls, user: User):
        user_profiles = user.profiles.all()
        queryset = cls.model.objects.all().select_related('user_profile')
        queryset = queryset.filter(user_profile__in=user_profiles)
        return queryset

    @classmethod
    def list_all_reports_by_user_and_state(cls, user: User, state: str):
        user_profiles = user.profiles.all()
        queryset = cls.model.objects.all().select_related('user_profile')
        queryset = queryset.filter(user_profile__in=user_profiles, state=state)
        return queryset
