from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    funds = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name + ": " + str(self.funds)
    
# class Transaction(model.Model):
#     account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
#     transaction_type = models.CharField(max_length=1)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)

class Budget(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    allocations = models.JSONField(default=dict)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


