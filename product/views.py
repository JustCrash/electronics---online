from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from company.models import Company
from product.models import Product
from product.paginators import ProductPaginator
from product.serializers import (ProductSerializer, ProductListSerializer,
                                 ProductDetailSerializer, ProductUpdateSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product view set.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPaginator

    def get_permissions(self):
        """
        Проверка доступа к продукту.
        """
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
        if self.action in ["list"]:
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = ProductListSerializer
        if self.action in ["retrieve"]:
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = ProductDetailSerializer
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = ProductUpdateSerializer
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Установив продукт в режим сериализатора, выполните создание.
        """
        product = serializer.save()
        company_customer = Company.objects.get(id=product.company.id)
        if company_customer.owner.id == self.request.user.id:
            product.save()
        else:
            product.delete()
            raise serializers.ValidationError("Вы не можете добавлять продукт в эту компанию")

    def perform_update(self, serializer):
        """
        Настройка продукта на сериализатор для выполнения обновления.
        """
        product = serializer.save()
        company_customer = Company.objects.get(id=product.company.id)
        if company_customer.owner.id == self.request.user.id:
            product.save()
        else:
            raise serializers.ValidationError("Вы не можете изменять продукт в этой компании")

    def perform_destroy(self, instance):
        """
        Установка продукта в сериализатор выполняет уничтожение.
        """
        company_customer = Company.objects.get(id=instance.company.id)
        if company_customer.owner.id == self.request.user.id:
            instance.delete()
        else:
            raise serializers.ValidationError("Вы не можете удалять продукт в этой компании")
