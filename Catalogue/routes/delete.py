from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import Record
from django.shortcuts import redirect


def delete_route(request, pk):
    rec = Record.objects.filter(catalogue_num=pk).first()
    if rec:
        rec.delete()
    return redirect("/")
