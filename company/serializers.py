from rest_framework import serializers

from company.models import Company
from company.models import Supplier


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
        fields = ("id", "name", "email", "country", "city", "street", "number_home", "owner")


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


class SupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов поставщика.
    """

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов обновления поставщика.
    """
    class Meta:
        model = Supplier
        fields = ('company_customer', 'company_supplier')


class SupplierListSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов списка поставщиков.
    """
    class Meta:
        model = Supplier
        fields = ('name_supplier', 'owner', 'id')
