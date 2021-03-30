from django.contrib import admin
from django.urls import path
from django.conf.urls import url

# Import the views of the Catalogue application so they can be routed to
from . import views


urlpatterns = [
    path("", views.search),
    # path("browse/", views.browse, name="browse"),
    path("items/", views.items, name="items"),
    path("login/", admin.site.urls, name="login"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/<str:pk>/", views.edit, name="edit"),
    path("logout/", views.logout, name="logout"),
    path("delete/<str:pk>/", views.delete, name="delete"),
]
