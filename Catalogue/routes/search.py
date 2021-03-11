from django.http import HttpResponse
from django.shortcuts import render
from Catalogue.models import Record
from django.db.models import Q


def search_route(request):
    if request.method == "GET":
        records = Record.objects.all()

        if "catalogue" in request.GET:
            catalogue = request.GET.__getitem__("catalogue")
            if catalogue:
                records = records.filter(item_type__icontains=catalogue).all()

        if "val" in request.GET:
            search_val = request.GET.__getitem__("val")
            if search_val:
                records = records.filter(
                    Q(name__icontains=search_val) | Q(description__icontains=search_val)
                )

        context = {"records": records}

        return render(request, "search.html", context)