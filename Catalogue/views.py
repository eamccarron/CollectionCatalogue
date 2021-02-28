from django.shortcuts import render
from django.http import HttpResponse
from .models import Fossil
from django.shortcuts import render
from django.views import View

# Create your views here.


def login(request):
    return render(request, "login.html")


def search(request):
    return render(request, "search.html")


def browse(request):
    context = {
        "records": [
            {
                "user": "Jared",
                "catalogue_number": "",
                "name": "Canon AE-1",
                "type": "camera",
                "date": "1990",
                "manufacturer": "Canon",
                "condition": "3",
                "provenance": "Inherited",
                "description": "This is my favourite piece in my collection",
                "additional_info": [("battery", "3V")],
                "has_image": True,
            },
            {
                "user": "Susan",
                "catalogue_number": "",
                "name": "Hasselblad 700",
                "type": "camera",
                "date": "1978",
                "manufacturer": "Hassbelblad",
                "condition": "4.5",
                "provenance": "Purchased new",
                "description": "Best camera",
                "additional_info": [("lens", "50mm")],
                "has_image": True,
            },
            {
                "user": "Will",
                "catalogue_number": "",
                "name": "Minolta X-700",
                "type": "camera",
                "date": "2001",
                "manufacturer": "Minolta",
                "condition": "2",
                "provenance": "Bought second hand",
                "description": "Decent camera.",
                "additional_info": [],
                "has_image": False,
            },
        ]
    }
    return render(request, "browse.html", context)
