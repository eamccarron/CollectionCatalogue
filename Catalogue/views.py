from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.views import View

from Catalogue.routes.browse import browse_route
from Catalogue.routes.login import login_route
from Catalogue.routes.search import search_route
from Catalogue.routes.create import create_route
from Catalogue.routes.items import item_route
from Catalogue.routes.edit import edit_route
from Catalogue.routes.delete import delete_route

from django.contrib.auth.decorators import login_required

from Catalogue.routes.logout import logout_route


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


@login_required
def edit(request, pk):
    return edit_route(request, pk)


@login_required
def delete(request, pk):
    return delete_route(request, pk)


def items(request):
    return item_route(request)


def logout(request):
    return logout_route(request)
