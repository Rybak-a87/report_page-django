from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    USER = ("user", "Пользователь")
    MANAGER = ("manager", "Менеджер")
    ADMINISTRATOR = ("administrator", "Администратор")
    STATUS_CHOICE = (
        USER, MANAGER, ADMINISTRATOR
    )
    role = models.CharField(
        verbose_name="Роль пользователя",
        max_length=30,
        choices=STATUS_CHOICE,
        null=True,
        blank=True
    )
