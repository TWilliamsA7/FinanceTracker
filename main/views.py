from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(response):
    if (response.user.is_authenticated):

        # Calculate the total funds acorss a user's accounts
        accounts = response.user.account_set.all()
        total = 0
        for account in accounts:
            total += account.funds

        params = {
            "username":response.user.username,
            "total_funds":total
        }

        return render(response, "main/index.html", params)
    else:
        return redirect("/login")
