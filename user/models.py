from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(models.AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="почта",
        help_text="Введите почту"
    )
    USERNAME_FIELD = email
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
