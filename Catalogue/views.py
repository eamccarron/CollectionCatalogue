from django.shortcuts import render
from django.http import HttpResponse
from .models import Fossil, BaseModel

from django.shortcuts import render
from django.views import View

# Create your views here.


def temp(request):
    context = {"entries": Fossil.objects.all()}
    return ""


def login(request):
    return render(request, "Catalogue/login.html")


def search(request):
    return render(request, "Catalogue/search.html")


def browse(request):
    context = {"records": BaseModel.objects.all()}
    return render(request, "Catalogue/browse.html", context)
