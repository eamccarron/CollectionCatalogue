from django.contrib import admin
from django.urls import path
#Import the views of the Catalogue application so they can be routed to
from . import views 



urlpatterns = [
    path("", views.index, name="Catalogue-Index"), #By default route to the home page (index)
    path("items/", views.items, name="Items") #route to page showing list of items in musuem
]