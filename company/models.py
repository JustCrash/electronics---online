from django.db import models
from user.models import Users


SUPPLIERS_TYPE = [("individual", "индивидуальный"), ("factory", "завод"), ("retail", "розничный"),]
NULLABLE = {"blank": True, "null": True}


class Company(models.Model):
    name = models.CharField(
        unique=True,
        max_length=250,
        verbose_name="Название",
        help_text="Укажите название",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
        help_text="Укажите адрес электронной почты",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Укажите страну",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Укажите город",
    )
    street = models.CharField(
        max_length=50,
        verbose_name="Улица",
        help_text="Укажите улицу",
    )
    number_home = models.CharField(
        max_length=10,
        verbose_name="Номер дома",
        help_text="Укажите номер дома",
    )
    level_company = models.IntegerField(
        default=0,
        verbose_name="Уровень компании",
    )
    type_company = models.CharField(
        max_length=20,
        choices=SUPPLIERS_TYPE,
        verbose_name="Тип компании",
    )
    supplier_name = models.CharField(
        max_length=100,
        verbose_name="Название поставщика",
        **NULLABLE,
    )
    supplier_id = models.IntegerField(
        verbose_name="Идентификатор поставщика",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Владелец компании",
        help_text="Укажите владельца компании",
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Supplier(models.Model):
    name_supplier = models.CharField(
        max_length=100,
        verbose_name="Название компании-поставщика",
        **NULLABLE
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Долг",
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    company_customer = models.IntegerField(
        verbose_name="Компания покупатель",

    )
    company_supplier = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
    )
    owner = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        **NULLABLE,
    )

    def __str__(self):
        return self.company_supplier

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
