from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

# Import the views of the Catalogue application so they can be routed to
from . import views


urlpatterns = [
    path("", views.browse),
    path("browse/", views.browse, name="browse"),
    path("login/", views.login, name="login"),
    path("search/", views.search, name="search"),
    path("accounts/", include("django.contrib.auth.urls")),
]
