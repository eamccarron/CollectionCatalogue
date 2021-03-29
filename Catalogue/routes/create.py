from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import Record
from ..forms import createNewRecord
from random import randint

# from django.db.models import Q


def create_route(request):
    # context = {"records": Record.objects.all()}
    if request.method == "GET":
        form = createNewRecord()
    else:  # POST
        form = createNewRecord(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            record_name = data["name"]
            num = randint(50, 1000)
            # create new record..........
            Record(name=record_name, catalogue_num=num).save()
        return HttpResponseRedirect("/browse?catalogue_num=%i" % num)
    return render(request, "create.html", {"form": form})
