from django.db import models

class Company(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Название",
        help_text="Укажите название"
    )
    contacts = models.IntegerField(
        max_length=11,
        verbose_name="Контактный телефон",
        help_text="Укажите контактный телефон"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
        help_text="Укажите адрес электронной почты"
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
        help_text="Укажите страну"
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Укажите город"
    )
    street = models.CharField(
        max_length=50,
        verbose_name="Улица",
        help_text="Укажите улицу"
    )
    number = models.CharField(
        max_length=10,
        verbose_name="Номер дома",
        help_text="Укажите номер дома"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
