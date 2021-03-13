from django.contrib import admin
from django.urls import path
from django.conf.urls import url

# Import the views of the Catalogue application so they can be routed to
from . import views


urlpatterns = [
    path("", views.browse),
    path("browse/", views.browse, name="browse"),
    path("login/", admin.site.urls, name="login"),
    path("search/", views.search, name="search"),
]