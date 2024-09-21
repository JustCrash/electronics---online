from django.db import models
from company.models import Company

class Product(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name="Название",
        help_text="Укажите название"
    )
    product_model = models.CharField(
        max_length=250,
        verbose_name="Модель",
        help_text="Укажите модель продукта"
    )
    create_date = models.DateTimeField(
        verbose_name="Дата выхода на рынок",
        help_text="Укажите дату выхода продукта на рынок"
    )
    company = models.ManyToManyField(
        Company,
        on_delete=models.CASCADE,
        verbose_name="Компания",
    )

    def __str__(self):
        return f"{self.name} ({self.product_model}) - {self.create_date}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
