
from django.http import HttpResponse
from django.shortcuts import render

def search_route(request):
    return render(request, "search.html")