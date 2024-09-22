from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from company.models import Company
from company.paginators import CompanyPaginator
from company.permissions import IsCompanyOwner

from company.serializers import CompanySerializer, CompanyDetailSerializer, CompanyListSerializer, \
    CompanyUpdateSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Company view set.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CompanyPaginator
    filter_backends = (filters.SearchFilter,)
    search_fields = ("country",)

    def get_permissions(self):
        """
        Проверка доступа к компании.
        """
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
            self.serializer_class = CompanySerializer
        if self.action in ["list"]:
            self.permission_classes = [AllowAny]
            self.serializer_class = CompanyListSerializer
        if self.action in ["retrieve"]:
            self.permission_classes = [IsAuthenticated, IsCompanyOwner]
            self.serializer_class = CompanyDetailSerializer
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsCompanyOwner]
            self.serializer_class = CompanyUpdateSerializer
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Создание объекта компании из сериализатора.
        """
        company = serializer.save()
        company.owner = self.request.user
        company.save()
        return company
