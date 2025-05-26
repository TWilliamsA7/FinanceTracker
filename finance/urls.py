from django.urls import path
from . import views

urlpatterns = [
    path("createbudget", views.createBudget, name="createbudget"),
    path("viewallbudgets", views.viewAllBudgets, name="viewallbudgets"),
    path("accounts", views.viewAccounts, name="accounts"),
    path("createaccount", views.createAccount, name="createaccount")
]