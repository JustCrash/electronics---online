from rest_framework import serializers

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов компании.
    """

    class Meta:
        model = Company
        fields = "__all__"


class CompanyListSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов списка компаний.
    """

    class Meta:
        model = Company
        fields = ("id", "name", "email", "country", "city", "street", "house_number", "owner")


class CompanyDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов сведений о компании.
    """

    class Meta:
        model = Company
        fields = "__all__"


class CompanyUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов обновления компании.
    """

    class Meta:
        model = Company
        fields = "__all__"
