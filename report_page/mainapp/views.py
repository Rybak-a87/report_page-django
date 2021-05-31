from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

from .models import EntryModel, StatisticModel
from .forms import CreateEntryForm
from .utils import add_to_statistic, filter_entries


User = get_user_model()


class ReadmeView(View):
    """представление страницы README"""
    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/readme.html")


class EntryListView(LoginRequiredMixin, ListView):
    """вывод записей"""
    login_url = '/'
    redirect_field_name = None

    model = EntryModel
    template_name = "mainapp/entries.html"
    context_object_name = "entries"
    ordering = "-date"

    def get_queryset(self):
        return filter_entries(self)


class StatisticListView(LoginRequiredMixin, ListView):
    """вывод статистики"""
    login_url = '/'
    redirect_field_name = None

    model = StatisticModel
    template_name = "mainapp/statistic.html"
    context_object_name = "weeks"
    ordering = ("-year", "-week_number")


class CreateEntry(LoginRequiredMixin, View):
    """создание записи"""
    login_url = '/'
    redirect_field_name = None

    def get(self, request, *args, **kwargs):
        form = CreateEntryForm(request.POST or None)
        context = {
            "form": form,
        }
        return render(request, "mainapp/create_entry.html", context)

    def post(self, request, *args, **kwargs):
        form = CreateEntryForm(request.POST or None)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.user = User.objects.get(username=self.request.user.username)
            new_entry.average_speed = round(form.cleaned_data["distance"] / form.cleaned_data["duration"], 2)
            new_entry.save()
            add_to_statistic(new_entry)
            return HttpResponseRedirect("/entries/")
        context = {
            "form": form,
        }
        return render(request, "mainapp/create_entry.html", context)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    """редактирование записи"""
    login_url = '/'
    redirect_field_name = None

    model = EntryModel
    template_name = "mainapp/create_entry.html"
    form_class = CreateEntryForm

    def form_valid(self, form):
        new = form.save(commit=False)
        new.average_speed = round(form.cleaned_data["distance"] / form.cleaned_data["duration"], 2)
        new.save()
        return HttpResponseRedirect("/entries/")


class EntryDetailView(DetailView):
    """вывод одной записи"""
    login_url = '/'
    redirect_field_name = None

    model = EntryModel
    context_object_name = "entry"
    template_name = "mainapp/entry_detail.html"
    pk_url_kwarg = "pk"


class EntryDeleteView(DeleteView):
    """удаление записи из базы данных"""
    login_url = '/'
    redirect_field_name = None

    model = EntryModel
    template_name = "mainapp/entry_delete.html"
    success_url = "/entries/"
