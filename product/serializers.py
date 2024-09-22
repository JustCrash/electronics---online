from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов продукта.
    """

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["arrears"]


class ProductListSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов списка продуктов.
    """

    class Meta:
        model = Product
        fields = ("id", "name", "product_model", "create_date", "company")


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов сведений о продукте.
    """

    class Meta:
        model = Product
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор объектов обновления продукта.
    """

    class Meta:
        model = Product
        fields = "__all__"
