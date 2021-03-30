from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import Record
from ..forms import createNewRecord, RecordForm
from django.db.models import Max


def create_route(request):
    if request.method == "GET":
        form = RecordForm()
    else:  # POST
        form = RecordForm(request.POST)

        if form.is_valid():
            args = Record.objects.all()
            if len(args) == 0:
                c_num = 1
            else:
                c_num = 1 + args.aggregate(Max("catalogue_num"))["catalogue_num__max"]
            form.instance.catalogue_num = c_num
            form.save()
            return HttpResponseRedirect("/items?catalogue_num=%i" % c_num)
    return render(request, "create.html", {"form": form})