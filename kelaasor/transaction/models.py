from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    balance = models.PositiveBigIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')