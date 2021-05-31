import datetime

from .models import StatisticModel
from .models import EntryModel


def str_to_date(text):
    """преобразование строки в дату"""
    if text:
        _temp = text.split("-")
        year = int(_temp[0])
        month = int(_temp[1])
        day = int(_temp[2])
        return datetime.date(year, month, day)
    else:
        return None


def filter_entries(obj):
    """реализация фильтра по диапазону даты"""
    start_date = str_to_date(obj.request.GET.get("start_date"))
    end_date = str_to_date(obj.request.GET.get("end_date"))
    if start_date and end_date:
        query = EntryModel.objects.filter(date__range=[start_date, end_date])
    elif start_date:
        query = EntryModel.objects.filter(date__gte=start_date)
    elif end_date:
        query = EntryModel.objects.filter(date__lte=end_date)
    else:
        query = EntryModel.objects.all()
    return query.order_by("-date")


def add_to_statistic(entry):
    """создание отчета и добавление записи в недельный отчет"""
    now_date = datetime.datetime.utcnow()
    data_date = now_date.isocalendar()

    statistic_week, created = StatisticModel.objects.get_or_create(
        week_number=data_date.week,
        year=data_date.year
    )
    statistic_week.entry.add(entry)
