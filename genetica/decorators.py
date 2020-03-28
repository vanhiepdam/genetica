# -*- coding: utf-8 -*-
from rest_framework.response import Response


def to_json_response(func):
    def inner(*args, **kwargs):
        data, status = func(*args, **kwargs)

        return Response(data=data, status=status)

    inner.__name__ = func.__name__

    return inner
