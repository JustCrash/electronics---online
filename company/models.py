from django.db import models


SUPPLIERS_TYPE = [("individual", "индивидуальный"), ("factory", "завод"), ("retail", "розничный"), ("null", "нет"),]


class Company(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Название",
        help_text="Укажите название",
    )
    contacts = models.IntegerField(
        max_length=11,
        verbose_name="Контактный телефон",
        help_text="Укажите контактный телефон",
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Supplier(models.Model):
    supplier = models.CharField(
        choices=SUPPLIERS_TYPE,
        verbose_name="Поставщик",
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
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
    )

    def __str__(self):
        return f"self.supplier"

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
