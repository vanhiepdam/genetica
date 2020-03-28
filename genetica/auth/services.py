# -*- coding: utf-8 -*-
from genetica.auth.models import User
from genetica.base.base_service import ServiceBase


class UserService(ServiceBase):
    model = User

    @classmethod
    def list_all_users(cls):
        return cls.model.objects.all()

    @classmethod
    def get_user_by(cls, **kwargs):
        return cls.model.objects.get(**kwargs)

    @classmethod
    def delete_user(cls, user_id):
        return cls.model.objects.delete(id=user_id)
