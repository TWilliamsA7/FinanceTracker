from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(response):
    if (response.user.is_authenticated):
        return render(response, "main/index.html", {})
    else:
        return redirect("/login")
