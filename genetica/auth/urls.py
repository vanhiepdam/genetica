# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from genetica.auth.views import UserViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewset, 'user')

urlpatterns = [
    url(r'1/', include(router.urls)),
    url(r'1/login', TokenObtainPairView.as_view(), name='obtain-token-pair'),
    url(r'1/token/refresh', TokenRefreshView.as_view(), name='refresh-token'),
    url(r'1/token/verify', TokenVerifyView.as_view(), name='verify-token'),
]

