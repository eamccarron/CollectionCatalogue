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
from Catalogue.routes.users import users_route

from Catalogue.routes.password_reset_complete import password_reset_complete_route
from Catalogue.routes.password_reset_confirm import password_reset_confirm_route
from Catalogue.routes.password_reset_done import password_reset_done_route
from Catalogue.routes.password_reset_email import password_reset_email_route
from Catalogue.routes.password_reset_form import password_reset_form_route
from Catalogue.routes.users import users_route

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

def password_reset_complete(request):
    return password_reset_complete(request)

def password_reset_confirm(request):
    return password_reset_confirm(request)

def password_reset_done(request):
    return password_reset_done(request)

def password_reset_email(request):
    return password_reset_email(request)

def password_reset_form(request):
    return password_reset_form(request)

@login_required
def users(request):
    return users_route(request)