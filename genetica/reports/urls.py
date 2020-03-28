# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from genetica.reports.views import ReportViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register('reports', ReportViewset, 'report')

urlpatterns = [
    url(r'1/', include(router.urls)),
]

