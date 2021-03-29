from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.views import View

from Catalogue.routes.browse import browse_route
from Catalogue.routes.login import login_route
from Catalogue.routes.search import search_route
from Catalogue.routes.create import create_route
from Catalogue.routes.items import item_route

from django.contrib.auth.decorators import login_required

# def temp(request):
#   context = {"entries": Fossil.objects.all()}
#  return ""

# View Declaration: Routes requests to appropriate files
def login(request):
    return login_route(request)


def search(request):
    return search_route(request)


def browse(request):
    return browse_route(request)


@login_required
def create(request):
    return create_route(request)


def items(request):
    return item_route(request)