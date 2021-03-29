from django import forms


class createNewRecord(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=False)
