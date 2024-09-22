from rest_framework import permissions


class IsCompanyOwner(permissions.BasePermission):
    """
    Проверяет, является ли пользователь владельцем компании.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsSupplierOwner(permissions.BasePermission):
    """
    Проверяет, является ли пользователь владельцем поставщика.
    """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
