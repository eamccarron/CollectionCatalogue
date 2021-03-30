from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import Record
from ..forms import createNewRecord


def item_route(request):
    records = Record.objects.all()
    if "catalogue_num" in request.GET:
        num = request.GET.__getitem__("catalogue_num")
        if num:
            records = records.filter(catalogue_num=num).all()

    context = {"records": records, "can_edit": request.user.is_authenticated}
    return render(request, "items.html", context)
