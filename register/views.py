from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(response):

    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
        return redirect("/")
    else:
        form = UserCreationForm()

    return render(response, "register/register.html", {"form":form})

def logout(response):
    return render(response, "register/logout.html", {})