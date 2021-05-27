from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class EntryModel(models.Model):
    """модель записи"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=255)
    distance = models.FloatField(verbose_name="Расстояние")
    duration = models.FloatField(verbose_name="Продолжительность времени")
    date = models.DateTimeField(verbose_name="Дата создания записи", auto_now=True)
    average_speed = models.FloatField(verbose_name="Средняя скорость")

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return "/entries/"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class StatisticModel(models.Model):
    """модель статистики"""
    week_number = models.PositiveIntegerField(verbose_name="Номер недели")
    total_entries = models.PositiveIntegerField(verbose_name="Количество записей")
    total_distance = models.FloatField(verbose_name="Общее расстояние")
    total_duration = models.FloatField(verbose_name="Общая продолжительность времени")
    average_speed = models.FloatField(verbose_name="Средняя скорость за неделю")

    def __str__(self):
        return f"{self.id}"
