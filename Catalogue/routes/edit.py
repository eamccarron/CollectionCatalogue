from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import *
from ..forms import *
from Catalogue.util import strToModel, strToForm
import time


def edit_route(request, pk):
    record = Record.objects.filter(catalogue_num=pk)

    if len(record) == 0:
        return HttpResponseRedirect("/")

    record = record[0]

    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()

            if form.instance.item_type in strToForm.keys():
                the_type = form.instance.item_type
                the_form = strToForm[the_type]
                the_obj = strToModel[the_type].objects.filter(record_id=pk)[0]
                obj = the_form(request.POST, instance=the_obj)
                obj.save()
            return HttpResponseRedirect(
                "/items?catalogue_num=%i" % form.instance.catalogue_num
            )
    else:
        form = RecordForm(instance=record)
        context = {"form": form, "catalogue_num": pk}

        if record.item_type in strToForm.keys():
            the_type = record.item_type
            if the_type in strToModel.keys():
                catalogue = strToModel[the_type]
                the_obj = catalogue.objects.filter(record_id=pk)
                if len(the_obj) == 0:
                    return HttpResponseRedirect("/")
                else:
                    the_obj = the_obj[0]
                extra = strToForm[the_type](instance=the_obj)
                context["extra"] = extra
    return render(request, "edit.html", context)