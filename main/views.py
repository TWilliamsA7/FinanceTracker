from django.shortcuts import render, redirect
from django.http import HttpResponse

from ast import literal_eval

def index(response):
    if (response.user.is_authenticated):

        # Calculate the total funds acorss a user's accounts
        accounts = response.user.account_set.all()
        monthlyBudget = response.user.budget_set.get(monthly=True)

        totalBudget = monthlyBudget.total
        monthlyBudgetAllo = monthlyBudget.allocations

        latestTrans = response.user.transaction_set.all().order_by("-date")[:7]


        monthlyBudgetLit = literal_eval(monthlyBudgetAllo)

        # A Post Request indicates a Reset Call
        if response.method == "POST":
            for section in monthlyBudgetLit:
                section["spent"] = 0.0
            monthlyBudget.allocations = str(monthlyBudgetLit)
            monthlyBudget.save()

        total = 0
        for account in accounts:
            total += account.funds

        params = {
            "username":response.user.username,
            "total_funds":total,
            "monthlyBudget":monthlyBudgetLit,
            "totalBudget":totalBudget,
            "latestTrans":latestTrans,
        }

        return render(response, "main/index.html", params)
    else:
        return redirect("/login")
