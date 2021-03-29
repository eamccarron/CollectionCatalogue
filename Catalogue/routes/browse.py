from django.http import HttpResponse
from django.shortcuts import render
from Catalogue.models import Fossil, Record


def browse_route(request):
    records = Record.objects.all()
    if "catalogue_num" in request.GET:
        num = request.GET.__getitem__("catalogue_num")
        if num:
            records = records.filter(catalogue_num=num).all()

    context = {"records": records}
    return render(request, "browse.html", context)