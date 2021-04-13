from django.http import HttpResponse
from django.shortcuts import render

def password_reset_complete_route(request):
    return render(request, "password_reset_complete.html")