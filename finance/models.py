from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    funds = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name + " " + str(self.funds)