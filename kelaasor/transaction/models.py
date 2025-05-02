from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    balance = models.PositiveBigIntegerField(default=0)


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    to = models.ForeignKey(Wallet, on_delete= models.CASCADE)
