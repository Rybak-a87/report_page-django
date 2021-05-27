from django.contrib import admin

from .models import EntryModel, StatisticModel


admin.site.register(EntryModel)
admin.site.register(StatisticModel)
