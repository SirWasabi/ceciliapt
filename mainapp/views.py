from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request, *args, **kwargs):
    return render(request, "index.html", {})


def contact(request, *args, **kwargs):
    return render(request, "contact.html", {})


def login(request, *args, **kwargs):
    return render(request, "login.html", {})
