from rest_framework import permissions


class IsCompanyOwner(permissions.BasePermission):
    """
    Проверяет, является ли пользователь владельцем компании.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
