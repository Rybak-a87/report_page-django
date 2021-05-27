from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, UpdateView
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

from .models import EntryModel, StatisticModel
from .forms import CreateEntryForm


User = get_user_model()


class ReadmeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/readme.html")


class EntryListView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = None

    model = EntryModel
    template_name = "mainapp/entries.html"
    context_object_name = "entries"


class StatisticListView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = None

    model = StatisticModel
    template_name = "mainapp/statistic.html"
    context_object_name = "weeks"


class CreateEntry(LoginRequiredMixin, View):
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
            return HttpResponseRedirect("/entries/")
        context = {
            "form": form,
        }
        return render(request, "mainapp/create_entry.html", context)


class EntryUpdateView(UpdateView):
    model = EntryModel
    template_name = "mainapp/create_entry.html"
    form_class = CreateEntryForm

    def form_valid(self, form):
        new = form.save(commit=False)
        new.average_speed = round(form.cleaned_data["distance"] / form.cleaned_data["duration"], 2)
        new.save()
        return HttpResponseRedirect("/entries/")
