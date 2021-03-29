from django.http import HttpResponse
from django.shortcuts import render

def logout_route(request):
    return render(request, "logout.html")