# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        field = view.lookup_field
        return getattr(request.user, field) == view.kwargs.get(field)


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        field = view.lookup_field
        return request.user.is_admin or getattr(request.user, field) == view.kwargs.get(field)
