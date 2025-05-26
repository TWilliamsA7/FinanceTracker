from django import forms
from .models import Account, Budget

class BudgetForm(forms.Form):
    name = forms.CharField(label="Budget Name", max_length=50)
    allocations_json = forms.CharField(widget=forms.HiddenInput)

class AccountForm(forms.Form):
    name = forms.CharField(label="Account Name", max_length=100)
    funds = forms.DecimalField(label="Funds", max_digits=10, decimal_places=2)

class TransactionForm(forms.Form):

    amount = forms.DecimalField(label="Amount", max_digits=10, decimal_places=2)
    account_id = forms.ModelChoiceField(label="Account", queryset=Account.objects.none())
    budget_id = forms.ModelChoiceField(label="Budget", required=False, queryset=Budget.objects.none())

    TYPE_CHOICES = [
        ('W', "Withdrawal"),
        ('D', "Deposit")
    ]

    transaction_type = forms.ChoiceField(label="Transaction Type", choices=TYPE_CHOICES)
    date = forms.DateField(label="Date")
    note = forms.CharField(label="Note", max_length=100)

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            print("Hello, World")
            self.fields['account_id'].queryset = Account.objects.filter(user_id=user)
            self.fields['budget_id'].queryset = Budget.objects.filter(user_id=user)