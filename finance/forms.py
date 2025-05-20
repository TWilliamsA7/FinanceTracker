from django import forms

class BudgetForm(forms.Form):
    name = forms.CharField(label="Budget Name", max_length=50)
    allocations_json = forms.CharField(widget=forms.HiddenInput)