
from django.http import HttpResponse
from django.shortcuts import render
from Catalogue.models import Fossil, Record

def browse_route(request):
    context = {"records": Record.objects.all()}
    return render(request, "browse.html", context)