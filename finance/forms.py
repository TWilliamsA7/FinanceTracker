from django import forms

class BudgetForm(forms.Form):
    name = forms.CharField(label="Budget Name", max_length=50)
    allocations_json = forms.CharField(widget=forms.HiddenInput)

class AccountForm(forms.Form):
    name = forms.CharField(label="Account Name", max_length=100)
    funds = forms.DecimalField(max_digits=10, decimal_places=2)
