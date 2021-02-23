from django.shortcuts import render
from django.http import HttpResponse
from .models import Fossil

# Create your views here.
def index(request):
    return HttpResponse(
        "<h1>Catalog Home Page.</h1> \n <p>This could handle login in and navigation to other parts of the website</p>"
    )


def items(request):
    theEntries = {"entries": Fossil.objects.all()}
    return render(request, "catalogue/items.html", theEntries)

    # fake change
