from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import Record
from ..forms import createNewRecord, RecordForm
import time


def edit_route(request, pk):
    rec = Record.objects.filter(catalogue_num=pk)

    if len(rec) == 0:
        return HttpResponseRedirect("/")

    rec = rec[0]

    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            rec.delete()
            time.sleep(2)
            form.save()
            return HttpResponseRedirect(
                "/items?catalogue_num=%i" % form.instance.catalogue_num
            )

    form = RecordForm(instance=rec)
    return render(request, "edit.html", {"form": form, "catalogue_num": pk})