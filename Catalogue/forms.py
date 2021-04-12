from django import forms
from django.forms import Form, CharField, ModelForm
from Catalogue.models import Record
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class createNewRecord(Form):
    name = CharField(label="Name", max_length=100, required=False)


class RecordForm(ModelForm):
        # other = CharField(label="other", max_length=100, required=False)

    class Meta:
        model = Record
        fields = [
            "item_type",
            "name",
            "date",
            "condition",
            "provenance",
            "description",
        ]
        widgets = {
            "item_type": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.TextInput(attrs={"class": "form-control"}),
            "condition": forms.TextInput(attrs={"class": "form-control"}),
            "provenance": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    is_superuser = forms.CheckboxSelectMultiple
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "is_superuser",)
        