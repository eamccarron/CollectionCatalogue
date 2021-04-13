from django import forms
from django.forms import Form, CharField, ModelForm
from Catalogue.models import *


def getFieldsWidgets(model):
    fields = []
    for f_name in model._meta.local_fields:
        fields.append(f_name.name)

    if "id" in fields:
        fields.remove("id")
    if "record" in fields:
        fields.remove("record")

    widgets = dict()
    for f in fields:
        widgets[f] = forms.TextInput(attrs={"class": "form-control"})
    return fields, widgets


class RecordForm(ModelForm):
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


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields, widgets = getFieldsWidgets(model)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields, widgets = getFieldsWidgets(model)


class CoinForm(ModelForm):
    class Meta:
        model = Coin
        fields, widgets = getFieldsWidgets(model)


class FossilForm(ModelForm):
    class Meta:
        model = Fossil
        fields, widgets = getFieldsWidgets(model)


class JewelryForm(ModelForm):
    class Meta:
        model = Jewelry
        fields, widgets = getFieldsWidgets(model)


class MedalForm(ModelForm):
    class Meta:
        model = Medal
        fields, widgets = getFieldsWidgets(model)


class MeteoriteForm(ModelForm):
    class Meta:
        model = Meteorite
        fields, widgets = getFieldsWidgets(model)


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields, widgets = getFieldsWidgets(model)


class PotteryForm(ModelForm):
    class Meta:
        model = Pottery
        fields, widgets = getFieldsWidgets(model)


class SculptureForm(ModelForm):
    class Meta:
        model = Sculpture
        fields, widgets = getFieldsWidgets(Sculpture)


class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields, widgets = getFieldsWidgets(model)


class OptionForm(ModelForm):
    class Meta:
        model = OptionalAttributes
        fields, widgets = getFieldsWidgets(model)