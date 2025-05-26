from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BudgetForm, AccountForm, TransactionForm
from .models import Budget, Account, Transaction

from ast import literal_eval

# Create your views here.

def viewAccounts(response):
    if (response.user.is_authenticated):

        accounts = response.user.account_set.all()

        return render(response, "finance/accounts.html", {'user':response.user, 'accounts':accounts})
    else:
        return redirect("/login")

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

def createAccount(response):
    if (response.user.is_authenticated):
        if (response.method == "POST"):
            form = AccountForm(response.POST)
            if form.is_valid():
                Account.objects.create(
                    name=form.cleaned_data['name'],
                    funds=form.cleaned_data['funds'],
                    user_id=response.user
                ).save()
                return redirect("accounts")
            print("Invalid Form")
            return redirect("/")
        else:
            form = AccountForm()
            return render(response, "finance/createaccount.html", {'user':response.user, 'form':form})
    else:
        return redirect("/login")
    
#  NEED TO MAKE TRANSACTIONS UPDATE THE ACCOUNTS TABLE

def viewTransactions(response):
    if (response.user.is_authenticated):

        if(response.method == "POST"): 
            form = TransactionForm(response.POST, user=response.user)
            if form.is_valid():
                Transaction.objects.create(
                    user_id = response.user,
                    account_id = form.cleaned_data['account_id'],
                    budget_id = form.cleaned_data['budget_id'],
                    transaction_type = form.cleaned_data['transaction_type'],
                    amount = form.cleaned_data['amount'],
                    note = form.cleaned_data['note'],
                    date = form.cleaned_data['date']
                ).save()

                acc = form.cleaned_data['account_id']
                if (form.cleaned_data['transaction_type'] == 'W'):
                    acc.funds -= form.cleaned_data['amount']
                else:
                    acc.funds += form.cleaned_data['amount']
                acc.save()

                return redirect("transactions")
            else:
                print("Invalid Form")
                return redirect("/")
        else:
            form = TransactionForm(user=response.user)
            transactions = response.user.transaction_set.all().order_by('-date', '-amount')
            return render(response, "finance/transactions.html", {'user':response.user, 'transactions':transactions, 'form':form})
    else:
        return redirect("/login")