from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BudgetForm
from .models import Budget

from ast import literal_eval

# Create your views here.

def viewAllBudgets(response):
    if (response.user.is_authenticated):

        budgets = response.user.budget_set.all()
        cleaned_data = {}
        for budget in budgets:
            cleaned_data[budget.name] = [literal_eval(budget.allocations), budget.total]
        
        cleaned_data = dict(sorted(cleaned_data.items()))

        return render(response, "finance/viewallbudgets.html", {'user':response.user, 'budgets':cleaned_data.items()})
    else:
        return redirect("/login")

def createBudget(response):
    if (response.user.is_authenticated):

        if (response.method == "POST"):
            form = BudgetForm(response.POST)
            if form.is_valid():

                ntotal = 0
                alloc = literal_eval(form.cleaned_data['allocations_json'])
                for d in alloc:
                    for v in d.values():
                        try:
                            ntotal += float(v)
                        except:
                            pass

                Budget.objects.create(
                    name=form.cleaned_data['name'],
                    user_id=response.user,
                    allocations=form.cleaned_data['allocations_json'],
                    total=ntotal
                ).save()
                return redirect("viewallbudgets")
            print("Invalid Form")
            return redirect("/")
        else:
            form = BudgetForm()
            return render(response, "finance/createbudget.html", {'form':form, 'username':response.user.username})
    else:
        return redirect("/login")

