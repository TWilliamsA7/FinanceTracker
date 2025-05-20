from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BudgetForm
from .models import Budget

# Create your views here.

def createBudget(response):
    if (response.user.is_authenticated):

        if (response.method == "POST"):
            form = BudgetForm(response.POST)
            if form.is_valid():
                Budget.objects.create(
                    name=form.cleaned_data['name'],
                    user_id=response.user,
                    allocations=form.cleaned_data['allocations_json']
                ).save()
                return redirect("/")
            print("Invalid Form")
            return redirect("/")
        else:
            form = BudgetForm()
            return render(response, "finance/createbudget.html", {'form':form})
    else:
        return redirect("/login")

