from rest_framework import serializers

from user.models import Users


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользовательских моделей.
    """
    class Meta:
        model = Users
        fields = ("email", "password",)


class UserListSerializer(serializers.ModelSerializer):
    """
    Сериализатор списков пользователей.
    """
    class Meta:
        model = Users
        fields = ("email",)
