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
    num_sections = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(15)
        ]
    )

    def __str__(self):
        return self.name + " Budget: " + self.num_sections + " Fields"

class Allocation(models.Model):
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    funds = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name + ": " + self.percentage + " | " + self.funds
