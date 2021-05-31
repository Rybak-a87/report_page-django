from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class EntryModel(models.Model):
    """модель записи"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=255)
    distance = models.FloatField(verbose_name="Расстояние")
    duration = models.FloatField(verbose_name="Продолжительность времени")
    date = models.DateTimeField(verbose_name="Дата создания записи", auto_now_add=True)
    average_speed = models.FloatField(verbose_name="Средняя скорость", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return "/entries/"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class StatisticModel(models.Model):
    """модель статистики"""
    year = models.PositiveSmallIntegerField(verbose_name="Год")
    week_number = models.PositiveSmallIntegerField(verbose_name="Номер недели")
    entry = models.ManyToManyField(EntryModel, verbose_name="Запись", blank=True)

    def __str__(self):
        return f"year: {self.year}, week: {self.week_number}"

    class Meta:
        verbose_name = "Статистику"
        verbose_name_plural = "Статистика"
