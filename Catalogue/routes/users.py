from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from Catalogue.forms import CustomUserCreationForm

def users_route(request):
    if request.method == "GET":
        return render(
            request, "users.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse("users"))
    