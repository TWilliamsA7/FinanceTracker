from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.utils.timezone import now

class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    funds = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name + ": " + str(self.funds)
    
class Budget(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    allocations = models.JSONField(default=dict)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    monthly = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    DEPOSIT = "D"
    WITHDRAWAL = "W"
    TRANSACTION_TYPE_CHOICES = {
        DEPOSIT: "Deposit",
        WITHDRAWAL: "Withdrawal"
    }

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    budget_id = models.ForeignKey(Budget, null=True, blank=True, on_delete=models.DO_NOTHING)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES, default=WITHDRAWAL)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=100)
    date = models.DateField(default=now)

    def __str__(self):
        return self.transaction_type + " " + str(self.amount) + ": " + self.note