from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.views import View

from Catalogue.routes.browse import browse_route
from Catalogue.routes.search import search_route
from Catalogue.routes.create import create_route
from Catalogue.routes.items import item_route
from Catalogue.routes.edit import edit_route
from Catalogue.routes.delete import delete_route
from Catalogue.routes.users import users_route
from Catalogue.routes.logout import logout_route
from Catalogue.routes.change_password import change_password_route

from django.contrib.auth.decorators import login_required

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

@login_required
def logout(request):
    return logout_route(request)

@login_required
def users(request):
    return users_route(request)

@login_required
def change_password(request):
    return change_password_route(request)