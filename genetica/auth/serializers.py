# -*- coding: utf-8 -*-
from rest_framework import serializers

from genetica.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    username = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        """Meta class.
        """
        model = User
        fields = (
            'id',
            'username',
            'email'
        )


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        """Meta class.
        """
        model = User
        fields = (
            'username',
            'email',
            'password'
        )


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        """Meta class.
        """
        model = User
        fields = (
            'email',
            'password'
        )
