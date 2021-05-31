from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    """Расширение полей модели пользователя"""
    MANAGER = ("manager", "Менеджер")
    ADMINISTRATOR = ("administrator", "Администратор")
    STATUS_CHOICE = (
        MANAGER, ADMINISTRATOR
    )
    role = models.CharField(
        verbose_name="Роль пользователя",
        max_length=30,
        choices=STATUS_CHOICE,
        null=True,
        blank=True
    )
