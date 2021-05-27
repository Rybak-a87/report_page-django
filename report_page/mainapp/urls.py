from django.urls import path
from . import views


app_name = "mainapp"


urlpatterns = [
    path("", views.ReadmeView.as_view(), name="readme_page"),
    path("entries/", views.EntryListView.as_view(), name="entries_page"),
    path("statistic/", views.StatisticListView.as_view(), name="statistic_page"),
    path("create-entry/", views.CreateEntry.as_view(), name="create_entry_page"),
    path("update-entry/<int:pk>/", views.EntryUpdateView.as_view(), name="update_entry_page"),
]
