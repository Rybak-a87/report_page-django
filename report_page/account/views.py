from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from .forms import LoginForm, RegistrationForm


class LoginView(View):
    """
    Авторизация пользователя
    """
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            "form": form,
            "title": "Авторизация"
        }
        return render(request, "account/login.html", context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/")
        context = {
            "form": form,
            "title": "Авторизация"
        }
        return render(request, "account/login.html", context)


class RegistrationView(View):
    """
    Регистрация пользователя
    """
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            "form": form,
            "title": "Регистрация"
        }
        return render(request, "account/login.html", context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data["username"]
            new_user.first_name = form.cleaned_data["first_name"]
            new_user.last_name = form.cleaned_data["last_name"]
            new_user.email = form.cleaned_data["email"]
            new_user.save()
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            user = authenticate(username=new_user.username, password=form.cleaned_data["password"])
            if user:
                login(request, user)
                return HttpResponseRedirect("/")

        context = {
            "form": form,
            "title": "Регистрация"
        }
        return render(request, "account/login.html", context)
