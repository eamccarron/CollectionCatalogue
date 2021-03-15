from django.http import HttpResponse
from django.shortcuts import render

def login_route(request):
    return render(request, "login.html")
