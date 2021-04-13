from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

# Import the views of the Catalogue application so they can be routed to
from . import views


urlpatterns = [
    path("", views.search),
    path("items/", views.items, name="items"),
    path("search/", views.search, name="search"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/change_password", views.change_password, name="change_password"),
    path("create/", views.create, name="create"),
    path("edit/<str:pk>/", views.edit, name="edit"),
    path("logout/", views.logout, name="logout"),
    path("delete/<str:pk>/", views.delete, name="delete"),
    path("users/",views.users, name="users"),
]
