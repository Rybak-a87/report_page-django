from django import forms

from .models import EntryModel


class CreateEntryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Название записи",
        "style": "margin-top: 20px;"
    }))
    distance = forms.FloatField(widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "Расстояние (километры)",
        "style": "margin-top: 20px;"
    }))
    duration = forms.FloatField(widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "Продолжительность времени (часы)",
        "style": "margin-top: 20px;"
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = ""
        self.fields["distance"].label = ""
        self.fields["duration"].label = ""

    class Meta:
        model = EntryModel
        fields = [
            "title",
            "distance",
            "duration",
        ]
