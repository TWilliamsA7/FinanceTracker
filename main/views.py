from django.shortcuts import render, redirect
from django.http import HttpResponse

from ast import literal_eval

def index(response):
    if (response.user.is_authenticated):

        # Calculate the total funds acorss a user's accounts
        accounts = response.user.account_set.all()
        monthlyBudget = response.user.budget_set.get(monthly=True)
        totalBudget = monthlyBudget.total
        monthlyBudget = monthlyBudget.allocations

        latestTrans = response.user.transaction_set.all().order_by("-date")[:7]

        monthlyBudget = literal_eval(monthlyBudget)

        total = 0
        for account in accounts:
            total += account.funds

        params = {
            "username":response.user.username,
            "total_funds":total,
            "monthlyBudget":monthlyBudget,
            "totalBudget":totalBudget,
            "latestTrans":latestTrans,
        }

        return render(response, "main/index.html", params)
    else:
        return redirect("/login")
